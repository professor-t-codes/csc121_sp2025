#
# Richard Tillies
# January 2, 2025
# Create class to define inventory items
#

CATEGORY_LIST = ["Book", "DVD", "Game"]


class InventoryItem:
    def __init__(self, name='', count=0, cost=0.0, category=''):
        self.__name = name
        self.__count = count
        self.__cost = cost
        self.__category = category

    def get_item_input(self):  # from Lab10P2.py
        # Get item name
        item_name = input('\nEnter the item name: ')

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
        print()

        # set object attributes
        self.__name = item_name
        self.__count = item_count
        self.__cost = unit_cost
        self.__category = category

    def __str__(self):
        output = f'{self.__name}\n' \
                 + f'\tCount: {self.__count}, Cost: {self.__cost:.2f}\n' \
                 + f'\tCategory: {self.__category}'

        return output
