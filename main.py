# Python Sales Calculator
# A beginner-friendly project for generating sales reports.

products = [
    {"name": "Keyboard", "price": 80, "quantity": 5},
    {"name": "Mouse", "price": 35, "quantity": 4},
    {"name": "Monitor", "price": 300, "quantity": 2},
    {"name": "Headphones", "price": 120, "quantity": 3}
]


def calculate_total(price, quantity):
    return price * quantity


def generate_sales_report(products):
    grand_total = 0

    print("=== SALES REPORT ===")

    for product in products:
        total = calculate_total(
            product["price"],
            product["quantity"]
        )

        grand_total += total

        print(product["name"], "-", total, "GEL")

    print("--------------------")
    print("Grand Total:", grand_total, "GEL")

    if grand_total >= 1000:
        print("Sales Target: Achieved")
    else:
        print("Sales Target: Not Achieved")


generate_sales_report(products)
