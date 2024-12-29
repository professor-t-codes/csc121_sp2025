#
# Student Name
# Assignment Date
# This program stores user-entered data into dictionaries and outputs
# the results.
#
CATEGORY_LIST = ['Book', 'DVD', 'Game']

def main():
    # TODO - Create three empty dictionaries named inventory_counts,
    #  inventory_costs, and inventory_categories

    print("Welcome to Trish's Inventory Input System")
    while True:
        item_name = get_item_name()
        item_count = get_item_count()
        unit_cost = get_unit_cost()
        category = get_category()

        # TODO - Add the item data to the three dictionaries. Use the item_name
        #  as a key for all dictionaries.
        #     - Add the item_count data as a value associated with the key
        #       item_name in inventory_counts.
        #     - Add the unit_cost data as a value associated with the key
        #       item_name in inventory_costs.
        #     - Add the category data as a value associated with the key
        #       item_name in inventory_categories.

        answer = ''
        while answer != 'y' and answer != 'n':
            answer = input('Enter another item? (y/n) ')
            answer = answer.lower()
            if answer != 'y' and answer != 'n':
                print('Enter y or n to continue.')
        if answer == 'n':
            break

    # TODO - Print the three dictionaries as shown in assignment's
    #  sample output.


def get_item_name():
    """
    Function to get an item name from the user.

    :return: The item name entered by the user.
    """
    # Get item name
    item_name = input('Enter the item name: ')
    return item_name


def get_item_count():
    """
    This function asks the user for an item count and
    validates it is greater than 0. It will continue
    asking for an item count until it is valid.

    :return: The validated item count entered by the user.
    """
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
    return item_count


def get_unit_cost():
    """
    This function asks the user for the unit cost and
    validates it is greater than 0. It will continue
    asking for the unit cost until it is valid.

    :return: The validated unit cost entered by the user.
    """
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost can only contain digits and a single decimal point.')
    return unit_cost


def get_category():
    """
    This function asks the user for a category and
    validates it is a valid category. It will continue
    asking for a category until it is valid.

    :return: The validated category entered by the user.
    :return:
    """
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return category


main()
