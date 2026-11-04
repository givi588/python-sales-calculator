# Automated Sales Report - USD

import csv
from pathlib import Path

folder = Path(__file__).resolve().parent

input_file = folder / "sales.csv"
output_file = folder / "sales_report.csv"

grand_total = 0
report_rows = []

try:
    with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required_columns = {"name", "price", "quantity"}

        if not required_columns.issubset(reader.fieldnames or []):
            raise ValueError("Required CSV columns are missing.")

        for product in reader:
            name = product["name"].strip()
            price = int(product["price"])
            quantity = int(product["quantity"])

            if not name or price < 0 or quantity < 0:
                raise ValueError("Invalid product data.")

            revenue = price * quantity
            grand_total += revenue

            report_rows.append({
                "name": name,
                "price": price,
                "quantity": quantity,
                "revenue": revenue
            })

    with open(output_file, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "price", "quantity", "revenue"]
        )

        writer.writeheader()
        writer.writerows(report_rows)

    print("=== AUTOMATED SALES REPORT ===")

    for product in report_rows:
        print(f"{product['name']} - ${product['revenue']}")

    print("-----------------------------")
    print(f"Grand Total: ${grand_total}")
    print(f"Report saved to: {output_file.name}")

except (FileNotFoundError, ValueError, KeyError, TypeError) as error:
    print("Error type:", type(error).__name__)
    print("Error details:", error)
