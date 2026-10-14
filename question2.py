def display_inventory(inventory):
    """Print every inventory item and its quantity."""
    for item, details in inventory.items():
        print(f"{item}: {details['quantity']}")


def calculate_total_value(inventory):
    """Return the total value of all inventory items."""
    total_value = 0

    for details in inventory.values():
        total_value += details["quantity"] * details["price"]

    return total_value


if __name__ == "__main__":
    inventory = {
        "Laptop": {"quantity": 5, "price": 85000},
        "Keyboard": {"quantity": 12, "price": 3500},
        "Mouse": {"quantity": 20, "price": 1800},
    }

    print("Inventory quantities:")
    display_inventory(inventory)
    print("Total inventory value:", calculate_total_value(inventory))