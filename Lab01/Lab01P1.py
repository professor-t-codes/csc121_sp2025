#
#  Author: Richard Tillies
#    Date: December 19, 2024
# Purpose: Display name, date, and information to the console
#

import datetime

name = input('What is your name? ')
print(f'Welcome to CSC121 {name}!')
print(f'Today is {datetime.date.today():%B %d, %Y}')
print('I hope you learn a lot of Python this semester!')
