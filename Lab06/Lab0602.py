##
# Richard Tillies
# December 20, 2024
# Creating tuples
#
from random import randint


def main():
    # Step A
    print('Step A:')
    count = int(input('How many values to put in the tuple? '))

    # Step B
    print('Step B:')
    lower = int(input('What is the start of the range? '))
    upper = int(input('What is the end of the range? '))

    # Step C
    first_list = []
    for c in range(count):
        first_list.append(randint(lower, upper))

    first_tuple = tuple(first_list)
    print(f'Step C: Tuple of {count} random numbers: {first_tuple}')

    # Step D
    first_four = slice(4)
    second_tuple = first_tuple[first_four]
    print(f'Step D: Tuple of first four numbers: {second_tuple}')

    # Step E
    last_two = slice(count - 2, count)
    third_tuple = first_tuple[last_two]
    print(f'Step E: Tuple of last two numbers: {third_tuple}')

    # Step F
    combined_tuple = third_tuple + second_tuple
    print(f'Step F: Two tuples concatenated: {combined_tuple}')

    # Step G
    second_list = list(combined_tuple)
    for i in range(len(second_list)):
        second_list[i] += 1

    incremented_tuple = tuple(second_list)
    print(f'Step G: Two tuples concatenated and incremented: {incremented_tuple}')

# Call main function
main()