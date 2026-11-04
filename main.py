# Python Sales Calculator - USD

products = [
    {"name": "Keyboard", "price": 30, "quantity": 5},
    {"name": "Mouse", "price": 25, "quantity": 4},
    {"name": "Monitor", "price": 150, "quantity": 2},
    {"name": "Headphones", "price": 60, "quantity": 3},
    {"name": "USB Cable", "price": 10, "quantity": 6}
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

        print(f"{product['name']} - ${total}")

    print("--------------------")
    print(f"Grand Total: ${grand_total}")

    if grand_total >= 700:
        print("Sales Target: Achieved")
    else:
        print("Sales Target: Not Achieved")


generate_sales_report(products)
