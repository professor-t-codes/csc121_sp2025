#
# Richard Tillies
# December 19, 2024
# Inventory Estimator
#

# Get the starting numbers of paperbacks and hardbacks.
books = int(input('What is the current number of books? '))
dvds = int(input('What is the current number of DVDs? '))
games = int(input('What is the current number of games? '))
print()

# Display the inventory stock table.
for month in range(0, 5):
    books += 45
    dvds += 32
    games += 15
    print(f'Month {month + 1}')
    print(f'\tBooks: {books}')
    print(f'\t DVDs: {dvds}')
    print(f'\tGames: {games}')

