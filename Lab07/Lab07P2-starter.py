#
# Student Name (Replace with your name)
# Assignment Date (Replace with the date)
# Count uppercase letters in a string
#
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
    print(line)   # DELETE THIS LINE

    # Strip the leading and trailing whitespace, and output the string.

    # Replace all occurrences of $NAME with your first name.

    # Replace all occurrences of $EMAIL with your email address.

    # Replace all occurrences of $CITY with the name of the city where you live.

    # Print the updated line.

    # Print a message indicating the number of characters in the updated line.

    # Count the number of occurrences of your first name and print a message
    # reporting the count.

    # Use floor division to divide the number of characters by 2, then print
    # the first half and last half of the line.

    # Print the line in uppercase.

    # Print the line in lowercase.


main()
