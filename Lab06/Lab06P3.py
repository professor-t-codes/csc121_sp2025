##
# Richard Tillies
# December 20, 2024
# List comprehension
#
def main():
    # Step A
    list1 = [4, 5, 8, 2]
    list2 = [2, 5, 9]

    # Step B: [-3, -1, 1, 3, 5, 7]
    list3 = [num * 2 - 3 for num in range(6)]
    print(f'Step B: {list3}')

    # Step C: [[1, 0], [1, 2], [1, 4], [3, 0], [3, 2], [3, 4]]
    list4 = [[[i,j] for j in range(5) if j % 2 == 0] for i in range(4) if i % 2 == 1]
    print(f'Step C: {list4}')

    # Step D: [64, 125, 512, 8]
    list5 = [i ** 3 for i in list1]
    print(f'Step D: {list5}')

    # Step E: [12, 15, 24, 6]
    list6 = [i * 3 for i in list1]
    print(f'Step E: {list6}')

    # Step F: [7, 19, 35, 9, 24, 44, 15, 39, 71, 3, 9, 17]
    list7 = [i * j - 1 for j in list2 for i in list1]
    print(f'Step F: {list7}')

    # Step G: ['4@2', '4@5', '4@9', '5@2', '5@5', '5@9', '8@2', '8@5', '8@9', '2@2', '2@5', '2@9']
    list8 = [f'{i}@{j}' for j in list2 for i in list1]
    print(f'Step G: {list8}')


# Call main function
main()