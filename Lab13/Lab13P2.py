#
# Richard Tillies
# January 4, 2025
# ITS Python Certification Review - Problem 2 (command line arguments)
#
import sys
from random import randint


def main():
    low, high, count = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    numbers = [randint(low, high) for i in range(count)]

    print(f'Grabbing {count} random numbers between {low} and {high}:')
    print(numbers)


# call main method
main()
