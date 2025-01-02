#
# Richard Tillies
# December 19, 2024
# Trish at Bargain Swap Shop has hired you to write a Python program that will help her calculate
# what a customer should pay. She has a very simple price structure:
# - Books are $2.25 each. Range 0-30
# - DVDs are $4.35 each. Range 0-15
# - Games are $5.00 each. Range 0-10
# - Sales tax 6.5%

# Variables
book_price = 2.25
dvd_price = 4.35
game_price = 5.0
tax_rate = 0.065
zero = 0
book_max = 30
dvd_max = 15
game_max = 10

# INPUT: Get the number of books. Range 0-30
books = int(input('Enter the number of books: '))
while books < zero or books > book_max:
    print(f'Number of books must be between {zero} and {book_max}')
    books = int(input('Enter the number of books: '))

# INPUT: Get the number of DVDs. Range 0-15
dvds = int(input('Enter the number of DVDs: '))
while dvds < zero or dvds > dvd_max:
    print(f'Number of DVDs must be between {zero} and {dvd_max}')
    dvds = int(input('Enter the number of DVDs: '))

# INPUT: Get the number of games. Range 0-10
games = int(input('Enter the number of games: '))
while games < zero or games > game_max:
    print(f'Number of games must be between {zero} and {game_max}')
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
