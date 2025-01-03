#
# Richard Tillies
# January 3, 2025
# Classes and OO Programming - Problem 2
#
import pickle
from inventory_item import InventoryItem, CATEGORY_LIST


def main():
    inventory_list = load_inventory()
    display_inventory(inventory_list)

    answer = ''
    while answer.lower() != 'n':
        # TODO - Create an InventoryItem object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list. HINT: Should be just 3 lines of code.
        new_item = InventoryItem()
        new_item.get_item_input()
        inventory_list.append(new_item)

        answer = input('Do you want to enter more items? ')

    for category in CATEGORY_LIST:
        display_category(category, inventory_list)

    display_inventory(inventory_list)
    save_inventory(inventory_list)


def load_inventory():
    """
    This function reads in a single list data structure from a
    binary file named inventory.dat and stores it in a variable
    that holds this inventory list data. The variable is returned.
    If the file does not exist, an empty list is returned.

    :return: List of InventoryItem objects representing the inventory
    """
    inventory_list = []
    # TODO - Attempt to load inventory data from a binary file named
    #  inventory.dat. If the file exists, load it into the inventory list.
    #  If the file does not exist, leave the inventory list empty.
    try:
        inventory = open('inventory.dat', 'rb')
        inventory_list = pickle.load(inventory)
        inventory.close()
    except FileNotFoundError:
        pass

    return inventory_list


def save_inventory(inventory_list):
    """
    This function takes the inventory list and saves it to a binary
    file named inventory.dat.

    :param inventory_list: List of all InventoryItem objects
    :return:
    """
    # TODO - Open a binary file named inventory.dat and dump the inventory
    #  list that has been passed in as a parameter to that file.
    inventory = open('inventory.dat', 'wb')
    pickle.dump(inventory_list, inventory)
    inventory.close()

    print('Inventory was saved in inventory.dat.')


def display_category(category_name, inventory_list):
    """
    This function displays all the inventory items in a specific
    category. The name of the category is displayed and the names
    of the items are shown below it.

    :param category_name: Categories of the items to be displayed
    :param inventory_list: List of all InventoryItems
    :return:
    """

    print()
    header = f'Items in {category_name}'
    divider = len(header) * '-'
    print(header)
    print(divider)
    # TODO - Display inventory items that are in the specific category
    #  Both the category name and inventory are passed in as parameters.
    #  If there are no items in the category, print "No items."
    for item in inventory_list:
        if item.get_category() == category_name:
            print(item)
        else:
            print("No items.")


def display_inventory(inventory_list):
    """
    This function displays all the inventory items in the inventory.
    Each item's attributes are shown on a single line.

    :param inventory_list: List of all InventoryItems
    :return:
    """

    print()
    print('Current Inventory')
    print('-----------------')
    # TODO - Display the inventory items that are in the inventory list
    #  that was passed in as a parameter. If the list is empty, display
    #  "Inventory is empty."
    if len(inventory_list) > 0:
        for item in inventory_list:
            print(item)
    else:
        print("Inventory is empty.")
    print('-----------------')
    #
    # print()


main()
