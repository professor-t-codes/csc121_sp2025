#
# Richard Tillies
# January 4, 2025
# Inheritance
#
# from Lab12.inventory_item import InventoryItem
from book import Book
from game import Game
from dvd import DVD


def main():
    inventory_list = []
    for i in range(3):
        answer = ''
        while answer not in ['1', '2', '3']:
            answer = input('What item type (1-Book, 2-Game, 3-DVD)? ')
            if answer not in ['1', '2', '3']:
                print('Enter 1, 2, or 3.')

        # TODO - Create an appropriate object, ask the user for item input
        #  using the object's method, then append the object to the inventory
        #  list.
        match answer:
            case '1':
                # print('Book')
                item = Book()
                # break
            case '2':
                # print('Game')
                item = Game()
                # break
            case _:  # case 3, input already validated 1-3
                # print('DVD')
                item = DVD()

        item.get_item_input()
        inventory_list.append(item)

    # Display inventory
    for item in inventory_list:
        print(item)


# call main method
main()
