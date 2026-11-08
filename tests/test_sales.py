"""Regression tests for the sample sales tools. No external dependencies."""

import contextlib
import csv
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from main import calculate_total, generate_sales_report


ROOT = Path(__file__).resolve().parents[1]


class SalesCalculatorTests(unittest.TestCase):
    def test_revenue_calculation(self):
        self.assertEqual(calculate_total(30, 5), 150)
        self.assertEqual(calculate_total(0, 10), 0)

    def test_report_target_achieved(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            generate_sales_report([{"name": "Item", "price": 100, "quantity": 7}])
        self.assertIn("Grand Total: $700", output.getvalue())
        self.assertIn("Sales Target: Achieved", output.getvalue())

    def test_report_target_not_achieved(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            generate_sales_report([{"name": "Item", "price": 50, "quantity": 1}])
        self.assertIn("Grand Total: $50", output.getvalue())
        self.assertIn("Sales Target: Not Achieved", output.getvalue())

    def test_main_script_output(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "main.py")],
            cwd=ROOT, capture_output=True, text=True, check=False
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Grand Total: $790", result.stdout)
        self.assertIn("Sales Target: Achieved", result.stdout)


class CsvAutomationTests(unittest.TestCase):
    def run_automation(self, csv_content=None):
        """Run a copied script in an isolated temporary directory."""
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            shutil.copyfile(ROOT / "automation.py", folder / "automation.py")
            if csv_content is not None:
                (folder / "sales.csv").write_text(csv_content, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(folder / "automation.py")],
                cwd=folder, capture_output=True, text=True, check=False
            )
            output_file = folder / "sales_report.csv"
            if output_file.exists():
                with output_file.open(newline="", encoding="utf-8") as f:
                    rows = list(csv.DictReader(f))
            else:
                rows = None
            return result, rows

    def test_original_sample_report(self):
        result, rows = self.run_automation((ROOT / "sales.csv").read_text(encoding="utf-8"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Grand Total: $790", result.stdout)
        self.assertEqual(len(rows), 5)
        self.assertEqual(rows[0], {"name": "Keyboard", "price": "30", "quantity": "5", "revenue": "150"})

    def test_whitespace_is_trimmed_from_names(self):
        result, rows = self.run_automation("name,price,quantity\n  Keyboard  ,10,2\n")
        self.assertEqual(rows[0]["name"], "Keyboard")
        self.assertEqual(rows[0]["revenue"], "20")

    def test_empty_report_is_supported(self):
        result, rows = self.run_automation("name,price,quantity\n")
        self.assertEqual(rows, [])
        self.assertIn("Grand Total: $0", result.stdout)

    def test_missing_input_reports_error_without_creating_output(self):
        result, rows = self.run_automation()
        self.assertIsNone(rows)
        self.assertIn("Error type: FileNotFoundError", result.stdout)

    def test_missing_required_columns_are_rejected(self):
        result, rows = self.run_automation("name,price\nKeyboard,10\n")
        self.assertIsNone(rows)
        self.assertIn("Required CSV columns are missing", result.stdout)

    def test_negative_quantity_is_rejected(self):
        result, rows = self.run_automation("name,price,quantity\nKeyboard,10,-2\n")
        self.assertIsNone(rows)
        self.assertIn("Invalid product data", result.stdout)

    def test_invalid_price_is_rejected(self):
        result, rows = self.run_automation("name,price,quantity\nKeyboard,oops,2\n")
        self.assertIsNone(rows)
        self.assertIn("Error type: ValueError", result.stdout)

    def test_blank_name_is_rejected(self):
        result, rows = self.run_automation("name,price,quantity\n ,10,2\n")
        self.assertIsNone(rows)
        self.assertIn("Invalid product data", result.stdout)


if __name__ == "__main__":
    unittest.main()
