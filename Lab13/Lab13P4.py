# Richard Tillies
# January 4, 2025
# ITS Python Certification Review - Problem 4 (datetime module)
#
import datetime


def main():
    current = datetime.datetime.now()

    print('The current date/time is:')
    print(f'{current.strftime("%x %I:%M:%S %p")}')
    print(f'{current.strftime("%A, %b %d, %Y")}')
    print(f'{current.strftime("%a, %B %d, %Y")}')

    string_format = '%m/%d/%Y'
    date_string = input("Enter a date (e.g. mm/dd/yyyy): ")
    try:
        date_convert = datetime.datetime.strptime(date_string, string_format)
        date_weekday = date_convert.strftime('%A')
        print(f'That date was on a {date_weekday}')
    except ValueError:
        print('Date in wrong format.')


# call main method
main()
