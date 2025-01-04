#
# Richard Tillies
# January 4, 2025
# Inheritance and Polymorphism - Problem 1 & 2
#
from inventory_item import InventoryItem


class DVD(InventoryItem):
    def __init__(self, item_name='', item_count=0, unit_cost=0.00, upc12='', genre=''):
        """
        This method is the class constructor. It sets the attributes of
        the class object with what is passed in by the calling routine.

        :param item_name: Name of item
        :param item_count: Number of item in inventory
        :param unit_cost: Unit cost of item
        :param upc12: UPC of the DVD
        :param genre: genre of the DVD
        """
        super().__init__(item_name, item_count, unit_cost, "Game")
        self.upc12 = upc12
        self.genre = genre

    def get_item_input(self):
        """
        This method will ask the user for item data and store it
        in the class object's attributes.

        :return:
        """
        # TODO - Call the base class get_item_input() using
        # the super() function.
        super().get_item_input()

        # TODO - Ask the user for the upc. Validate that
        # it is all digits and has 12 characters

        while True:
            try:
                upc = input('What is the UPC? ')
                if len(upc) != 12:
                    print('UPC must be a 12 digit number (length).')
                else:
                    valid = int(upc)
                    self.upc12 = upc
                    break
            except ValueError:
                print('UPC must be a 12 digit number (int).')

        # TODO - Ask the user for the genre.
        self.genre = input("What is the genre of the DVD? ")

        # pass  # Remove this line

    def __str__(self):
        """
        This method will return a human-readable version of the
        class object.

        :return: Human-readable string representing the object.
        """

        return (super().__str__() + '\n' +
                f'\tUPC: {self.upc12} \n' +
                f'\tGenre: {self.genre}')
