##
# Richard Tillies
# December 19, 2024
# Simulate a game by rolling a special die
#
from random import randint


def main():
    num_rolls = int(input('How many times do you want to roll the die? '))
    while num_rolls < 5 or num_rolls > 15:
        print('Enter a number between 5 and 15.')
        num_rolls = int(input('How many times do you want to roll the die? '))

    roll_die(num_rolls)

def roll_die(rolls):
    for roll in range(rolls):
        value = randint(1,20)
        if value == 20:
            symbol = 'CRITICAL HIT!'
        elif value % 4 == 0:
            symbol = 'Sword'
        elif value % 4 == 1:
            symbol = 'Shield'
        elif value % 4 == 2:
            symbol = 'Spell'
        else:
            symbol = 'Potion'

        print(f'Roll {roll}: {value} ==> {symbol}')

    print('Thanks for playing!')

# call main function
main()