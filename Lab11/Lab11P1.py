#
# Richard Tillies
# January 2, 2025
# Demo class for inventory
#
from Lab11.inventory_item import InventoryItem


def main():
    # Create three objects
    python = InventoryItem("Python for All", 10, 12.95, "Book")
    barbie = InventoryItem("Barbie", 15, 6.95, "DVD")
    uno = InventoryItem("Uno", 32, 4.5, "Game")

    # Display objects in console using __str__ method
    print(python)
    print(barbie)
    print(uno)

    # Cr
    new_item = InventoryItem()
    new_item.get_item_input()
    print(new_item)

main()
