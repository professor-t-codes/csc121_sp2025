#
# Richard Tillies
# January 1, 2025
# Starter Code for Lab 10 Problem 2 (Remove this line before submitting)
# Trish's Bookstore Inventory System
#
import pickle
CATEGORY_LIST = ['Book', 'DVD', 'Game']
FILENAME = 'inventory.dat'

# Review the main() function and update TODO sections.
# Do not change any other code within main().
def main():
    inventory_counts, inventory_costs, inventory_categories = read_inventory_file()

    print("Welcome to Trish's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    response = ''
    while response != '0':
        display_menu()
        response = input('Enter your choice: ')

        if response == "1":  # Add an item
            item_name, item_count, unit_cost, category = get_item_input()
            # TODO - Replace pass with code that will add the item_name,
            #  item_count, and unit_cost data to the dictionaries
            # pass
            inventory_counts[item_name] = item_count
            inventory_costs[item_name] = unit_cost
            inventory_categories[item_name] = category
            print(f'{item_name} added to inventory.')
        elif response == "2":  # Display a single item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will display the item data
            #  from the dictionaries or display "Not found"
            # pass
            if item_name in inventory_counts:
                print(item_name)
                print(f'\tCount: {inventory_counts[item_name]}, Cost: {inventory_costs[item_name]:.2f}')
                print(f'\tCategory: {inventory_categories[item_name]}\n')
            else:
                print(f'{item_name}: Not found')
        elif response == "3":  # Display items in a category
            category_name = input('Enter category name: ')
            if category_name in CATEGORY_LIST:
                # TODO - Replace pass with code that will print the names
                #  of all the items in the category
                # pass
                print(f'\nItems in {category_name}:')
                for item in inventory_categories:
                    if inventory_categories[item] == category_name:
                        print(f'\t{item}')
            else:
                print(f'{category_name} not in list of categories: {CATEGORY_LIST}')
            print()
        elif response == "4":  # Delete a single item
            item_name = input('Enter item name: ')
            # TODO - Replace pass with code that will remove the item data
            #  from the dictionaries or display "Not found"
            # pass
            if item_name in inventory_counts:
                inventory_counts.pop(item_name)
                inventory_costs.pop(item_name)
                inventory_categories.pop(item_name)
                print(f'{item_name} deleted.')
            else:
                print(f'{item_name}: Not found')
            print()

        elif response == "5":  # Display all inventory
            # TODO - Replace pass with code that will display all the inventory
            #  items - HINT Don't we already have a function that does that?
            # pass
            display_all_inventory(inventory_counts, inventory_costs, inventory_categories)
        elif response != "0":
            print("Invalid choice. Try again.\n")
        # print()

    # Ready to exit the program, display and save inventory as last steps
    print("Final Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    save_inventory_file(inventory_counts, inventory_costs, inventory_categories)


def display_menu():
    """
    This function displays a menu of options for the user.

    :return:
    """
    print("What would you like to do?")
    print("(1) Add an item\n"
          "(2) Display an item\n"
          "(3) Display a category\n"
          "(4) Delete an item\n"
          "(5) Display all inventory\n"
          "(0) Exit")


def display_all_inventory(inventory_counts, inventory_costs, inventory_categories):
    """
    This function displays all of the inventory items. If there is no
    inventory, the function displays "== Empty ==". Note that all the
    dictionaries should have the same keys which represent the item
    names.

    :param inventory_counts: Dictionary of item counts
    :param inventory_costs: Dictionary of item costs
    :param inventory_categories: Dictionary of item categories.
    :return:
    """

    # TODO - Replace pass with code that will iterate through the dictionaries
    #  that are passed in and display the inventory. If the dictionaries are
    #  empty the display "== Empty =="
    # pass
    # print('Current Inventory')
    if len(inventory_counts) > 0:
        print(f'Item name      Count   Unit Cost  Category')
        print(f'---------      -----   ---------  --------')
        for key in inventory_counts:
            print(f'{key:14} {inventory_counts[key]:5} {inventory_costs[key]:11.2f}  {inventory_categories[key]:20} ')
    else:
        print("== Empty ==")
    print()

def save_inventory_file(inventory_counts, inventory_costs, inventory_categories):
    """
    This function saves the 3 input dictionaries in a binary file named
    inventory.dat.

    :param inventory_counts: Dictionary of item counts
    :param inventory_costs: Dictionary of item costs
    :param inventory_categories: Dictionary of item categories.
    :return:
    """

    # TODO - Replace pass with code that will save your dictionaries to
    #  inventory.dat using the pickle module.
    # pass
    # filename = 'inventory.dat'
    inventory = open(FILENAME, 'wb')
    pickle.dump(inventory_counts, inventory)
    pickle.dump(inventory_costs, inventory)
    pickle.dump(inventory_categories, inventory)
    inventory.close()

    print(f'Inventory saved to {FILENAME}')

def read_inventory_file():
    """
    This function reads in 3 dictionaries from a binary file named
    inventory.dat and returns those dictionaries to the calling
    routine. If the file does not exist, it returns 3 empty dictionaries.

    :return: Current inventory in 3 dictionaries.
    """

    inventory_counts = {}
    inventory_costs = {}
    inventory_categories = {}
    # TODO - Replace pass with code that will read your dictionaries from
    #  inventory.dat using the pickle module.
    # pass
    # return inventory_counts, inventory_costs, inventory_categories
    try:
        inventory = open('inventory.dat', 'rb')
        inventory_counts = pickle.load(inventory)
        inventory_costs = pickle.load(inventory)
        inventory_categories = pickle.load(inventory)
    except FileNotFoundError:
        pass
    return inventory_counts, inventory_costs, inventory_categories


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    """
    This function asks the user for the name, count, cost, and category
    for a particular item and returns those values to the calling
    routine. It validates that count, cost, and category are acceptable
    values and prompts the user if there are any issues.

    :return: Name, count, cost, and category entered by user (validated)
    """

    # Get item name
    item_name = input('Enter the item name: ')
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost must be an integer.')
    # Get category
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return item_name, item_count, unit_cost, category


main()
