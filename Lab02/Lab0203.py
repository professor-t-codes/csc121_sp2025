#
# Richard Tillies
# December 19, 2024
# Trish at Bargain Swap Shop has decided to add a gift card program for her loyal customers and
# for customers that buy a lot. Here's how it works:
# - If a customer is in her loyalty program AND they buy $50-100, they get a $15 gift card.
# - If a customer is in her loyalty program AND they buy over $100, they get a $25 gift card.
# - If a customer is not in her loyalty program but they buy over $100, they get a $5 gift card.
# Note: Some customers aren’t eligible for a gift card. The program should indicate that.
# With every purchase, Trish also must charge 6.5% sales tax on the total. The gift card is NOT
# included in the total and is not considered when calculating the tax.
#

tax_rate = 0.065
gift_card = 0
is_loyalty = False

# INPUT: Get the number of books, DVDs, and games.
purchase_amount = float(input('Enter the total purchase amount: $'))
loyalty = input('Is the customer a loyalty program member? (y/n) ')

# PROCESSING: Calculate the amount of sales tax and total after tax
sales_tax = purchase_amount * tax_rate
total_after_tax = purchase_amount + sales_tax

# PROCESSING: Determine loyalty membership
# is_loyalty = True if loyalty == 'y' else False
if loyalty == 'y':
    is_loyalty = True

# PROCESSING: Determine gift card amount, if applicable
if is_loyalty and purchase_amount > 100:
    gift_card = 25
elif is_loyalty and purchase_amount >= 50:
    gift_card = 15
elif not is_loyalty and purchase_amount > 100:
    gift_card = 5

# OUTPUT: Display the total before tax, amount of sales tax, and total after tax
print(f'Sales tax: ${sales_tax:,.2f}')
print(f'Total after tax: ${total_after_tax:,.2f}')
print(f'Gift Card Awarded: ${gift_card}')
