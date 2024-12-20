##
# Richard Tillies
# December 20, 2024
# Count uppercase letters in a string
##
import os

# DO NOT CHANGE ANY CODE IN THE MAIN FUNCTION
def main():
    try:
        input_file = open('strings.txt', 'r')  # Open a file for reading
        for line in input_file:  # Use a for loop to read each line in the file
            manipulate_text(line)
            print()
    except FileNotFoundError:
        print('Did not find strings.txt in current directory:')
        print(os.getcwd())


def manipulate_text(line):
    """
    This function accepts a string, performs various manipulations on the
    string, and outputs the results. It demonstrates many different str
    methods, operators, and functions from Lesson 7 of CSC-121.

    :param line: A text string to be manipulated
    :return:
    """
    # print(line)   # DELETE THIS LINE
    name = 'Richard'
    email = 'rtillies@waketech.edu'
    city = 'Raleigh, NC'

    # Strip the leading and trailing whitespace, and output the string.
    line = line.strip()
    print('Original line:', line)

    # Replace all occurrences of $NAME with your first name.
    line = line.replace('$NAME', name)

    # Replace all occurrences of $EMAIL with your email address.
    line = line.replace('$EMAIL', email)

    # Replace all occurrences of $CITY with the name of the city where you live.
    line = line.replace('$CITY', city)

    # Print the updated line.
    print('Updated line:', line)

    # Print a message indicating the number of characters in the updated line.
    print(f'Number of characters in updated line: {len(line)}')

    # Count the number of occurrences of your first name and print a message
    # reporting the count.
    print(f'Occurrences of {name}: {line.count(name)}')

    # Use floor division to divide the number of characters by 2, then print
    # the first half and last half of the line.
    print(f'First half of line: {line[0:len(line) // 2]}')
    print(f'Second half of line: {line[len(line) // 2:]}')

    # Print the line in uppercase.
    print('Line in uppercase:', line.upper())

    # Print the line in lowercase.
    print('Line in lowercase:', line.lower())

# Call main function
main()
