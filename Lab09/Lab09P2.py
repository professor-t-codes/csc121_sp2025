#
# Richard Tillies
# December 29, 2024
# Python sets
#
from random import randint


def main():
    # Create two sets
    set1 = generate_set(8) # max_value = 16
    set2 = generate_set(8) # max_value = 16

    # Print set1 and set2
    print(f'set1: {set1}')
    print(f'set2: {set2}')

    # Print union, intersection, difference, and symmetric difference of set1 and set2
    print(f'Union of set1 and set2: {set1.union(set2)}')
    print(f'Intersection of set1 and set2: {set1.intersection(set2)}')
    print(f'Difference of set1 and set2: {set1.difference(set2)}')
    print(f'Symmetric difference of set1 and set2: {set1.symmetric_difference(set2)}')

    # Print items in union of set1 and set2 that are less than 10
    set3 = less_than_set(set1.union(set2)) # max value = 10
    print(f'Less than 10 in union of set1 and set2: {set3}')

# Create a set with up to 8 random numbers between 1 and max value (default: 16)
def generate_set(count, max_value = 16):
    new_set = set()
    for i in range(count):
        new_set.add(randint(1, max_value))

    return new_set

# Create a set with values less than max value (default: 10)
def less_than_set(input_set, max_value = 10):
    set3 = set()
    for item in input_set:
        if item < max_value:
            set3.add(item)

    return set3

# Call main function
main()
