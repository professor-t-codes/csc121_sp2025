#
# Student Name
# Date
# ITS Python Certification Review - Problem 1 (string format method)
#
TAX_RATE = 0.07

def main():
    title = 'From Here to Python'
    price = 4.50
    count = 7

    # TODO: Convert these 4 output statements so they are using f-strings
    #  instead of the string format method
    print('We have {0} copies of the book.'.format(count))
    # Comment out the line above and put your conversion on the next line
    
    print('The {0} copies cost {1:.2f} each.'.format(count, price))
    # Comment out the line above and put your conversion on the next line

    print('Title: {2}\nCount: {0}\nPrice: {1:.2f}'.format(count, price, title))
    # Comment out the line above and put your conversion on the next line

    print('The tax on {0:.2f} is {1:.2f}.'.format(price, price * TAX_RATE))
    # Comment out the line above and put your conversion on the next line


    print()

    # TODO: Convert these 4 output statements so they are using the string
    #  format method instead of f-strings
    print(f'The title of the book is {title}.')
    # Comment out the line above and put your conversion on the next line

    print(f'"{title}" costs {price:.2f}')
    # Comment out the line above and put your conversion on the next line

    print(f'We have {count} copies of "{title}" in stock.')
    # Comment out the line above and put your conversion on the next line

    print(f'To buy all {count} copies of "{title}" will cost {count * price:.2f}')
    # Comment out the line above and put your conversion on the next line


main()
