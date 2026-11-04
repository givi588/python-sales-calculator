# Python Sales Calculator

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
- Automated tests
- Monthly sales reporting

## Author

GitHub: [givi588](https://github.com/givi588)
