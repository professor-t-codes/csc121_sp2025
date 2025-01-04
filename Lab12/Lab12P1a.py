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
    python1 = Book('Python Now', 100, 22.95, '2345234523451')
    python2 = Book('Even More Python', 150, 8.95, '3456345634561')
    uno = Game('Uno', 75, 6.95, '123456789012')
    barbie = DVD('Barbie', 50, 12.0, '098765432121', 'Comedy')
    piano = DVD('The Piano', 10, 2.9, '321321321321', 'Drama')

    print(python1)
    print(python2)
    print(uno)
    print(barbie)
    print(piano)


# call main method
main()
