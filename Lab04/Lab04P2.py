##
# Richard Tillies
# December 19, 2024
# Trish's Swap Shop Calculator
#
# Global Constants
BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
TAX_RATE = 0.065  # Tax Rate of 6.5%

def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_books = int(input('Enter the number of books: '))
    num_dvds = int(input('Enter the number of DVDs: '))
    num_games = int(input('Enter the number of games: '))

    calc_and_display_total(num_books, num_dvds, num_games)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    books  - Number of books
#    dvds  - Number of dvds
#    games  - Number of games
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.

def calc_and_display_total(books, dvds, games):
    book_cost = books * BOOK_PRICE
    dvd_cost = dvds * DVD_PRICE
    game_cost = games * GAME_PRICE

    cost_before_tax = book_cost + dvd_cost + game_cost
    sales_tax = cost_before_tax * TAX_RATE
    cost_after_tax = cost_before_tax + sales_tax

    print(f'Books: ${book_cost:.2f}')
    print(f'DVDs: ${dvd_cost:.2f}')
    print(f'Games: ${game_cost:.2f}')

    print(f'Subtotal: ${cost_before_tax:.2f}')
    print(f'Tax: ${sales_tax:.2f}')
    print(f'Total: ${cost_after_tax:.2f}')

main()
