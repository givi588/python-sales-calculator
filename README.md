# Python Sales Calculator

[![Python tests](https://github.com/givi588/python-sales-calculator/actions/workflows/python-tests.yml/badge.svg)](https://github.com/givi588/python-sales-calculator/actions/workflows/python-tests.yml)

A beginner-friendly Python project for calculating sales revenue and automating CSV reports in USD.

## Features

- Calculate revenue for multiple products
- Generate sales reports in USD
- Evaluate sales targets
- Read product data from CSV files
- Automatically generate a new CSV report
- Validate basic product data

## Technologies

- Python 3
- Python CSV Module
- pathlib
- No external libraries required

## Project Files

- `main.py` - Basic sales calculator
- `automation.py` - Automated CSV report generator
- `sales.csv` - Sample product data
- `sales_report.csv` - Generated output (created when the automation runs)

## How to Run

Install Python 3 and download this repository.

### Basic Calculator

```bash
py main.py
```

### CSV Automation

```bash
py automation.py
```

The automation reads `sales.csv` and creates `sales_report.csv`.

## Example Output

```text
=== AUTOMATED SALES REPORT ===
Keyboard - $150
Mouse - $100
Monitor - $300
Headphones - $180
USB Cable - $60
-----------------------------
Grand Total: $790
Report saved to: sales_report.csv
```

## Tests and continuous integration

The [GitHub Actions workflow](.github/workflows/python-tests.yml) checks Python syntax and runs the test suite on Python **3.11, 3.12, and 3.13** whenever code is pushed to `main` or a pull request is opened.

Run the same tests locally without installing dependencies:

```bash
py -m unittest discover -s tests -v
```

On macOS/Linux use `python3 -m unittest discover -s tests -v`.

The **12 tests** cover revenue calculations, the sales-target threshold, command-line output, valid CSV reports, and rejection of invalid CSV data. CSV automation tests run on temporary copies and do not overwrite the sample report. A passing status only certifies that these checks ran successfully; it is not a guarantee that the tool is suitable for production accounting.

`main.py` can be imported without printing or running a report automatically; executing it directly still prints the example report. The CSV report script still expects integer prices and quantities and prints errors rather than exiting with a failure code.

## Learning Goals

This project demonstrates:

- Variables and data types
- Lists and dictionaries
- Functions
- For loops and conditions
- CSV file processing
- Basic error handling
- Business process automation

## Future Improvements

- Configurable currency and sales targets
- Better input validation
- Support for decimal prices
- Additional input-validation rules and error exit codes
- Monthly sales reporting

## Author

GitHub: [givi588](https://github.com/givi588)
