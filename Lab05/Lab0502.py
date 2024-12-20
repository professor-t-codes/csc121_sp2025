##
# Richard Tillies
# December 20, 2024
# Create and manipulate lists in Python
#
from random import randint

# Step A
count = int(input('Step A: How many numbers in each list? '))

# Step B
print('Step B:')
lower = int(input('What is the lower bound for the random numbers? '))
upper = int(input('What is the upper bound for the random numbers? '))

# Step C
first_list = []
for c in range(count):
    first_list.append(randint(lower,upper))

print(f'Step C: First List: {first_list}')

# Step D
second_list = []
for c in range(count):
    second_list.append(randint(lower,upper))

print(f'Step D: Second List: {second_list}')

# Step E
print('Step E:')
for c in range(count):
    print(first_list[c], second_list[c])

# Step F
combined_list = first_list + second_list
print(f'Step F: Combined list: {combined_list}')

# Step G
combined_list.sort()
print(f'Step G: Sorted list: {combined_list}')

# Step H
print('Step H:')
print(f'First three elements: {combined_list[0:3]}')
print(f'Last three elements: {combined_list[-3:]}')

# Step I
print(f'Step I: Sum: {sum(combined_list)}')

# Step J
print(f'Step J: Minimum: {min(combined_list)}')

# Step K
print(f'Step K: Maximum: {max(combined_list)}')

# Step L
print('Step L:')
for i in range(5):
    number = randint(lower, upper)
    try:
        index = combined_list.index(number)
        print(number, 'at index', index)
        combined_list.remove(number)
    except ValueError:
        print(number, 'not found in list')

# Step M
print(f'Step M: Final list: {combined_list}')