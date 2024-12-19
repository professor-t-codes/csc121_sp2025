#
# Richard Tillies
# December 19, 2024
# Trish at Bargain Swap Shop has hired you to write a Python program that will help her calculate
# what a customer should pay. She has a very simple price structure:
# - Books are $2.25 each.
# - DVDs are $4.35 each.
# - Games are $5.00 each.
# - Sales tax 6.5%

book_price = 2.25
dvd_price = 4.35
game_price = 5.0
tax_rate = 0.065

# INPUT: Get the number of books, DVDs, and games.
books = int(input('Enter the number of books: '))
dvds = int(input('Enter the number of DVDs: '))
games = int(input('Enter the number of games: '))

# PROCESSING: Calculate the total before tax, amount of sales tax, and cost after tax
cost_before_tax = \
    (books * book_price) + \
    (dvds * dvd_price) + \
    (games * game_price)

sales_tax = cost_before_tax * tax_rate

cost_after_tax = cost_before_tax + sales_tax

# OUTPUT: Display the total before tax, amount of sales tax, and cost after tax
print(f'Cost before tax: ${cost_before_tax:,.2f}')
print(f'Sales tax: ${sales_tax:,.2f}')
print(f'Cost after tax: ${cost_after_tax:,.2f}')
