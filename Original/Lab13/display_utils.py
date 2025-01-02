#
# Provided by WT Instructors
# 8/5/2024
# This module will display various messages as indicated
# in the function comments.
#

def get_user_greeting(name):
    """
    This function will return a greeting for the user
    whose name is passed in to the function.

    :param name: Name to be greeted
    :return: The greeting including the name
    """

    # This line has a bug which should be caught
    # by the automated testing!
    return f'Hello-{name}!'

def sum_is_greater(first, second, third):
    """
    This function will return True if the first two
    parameters added together are greater than the third
    parameter.

    :param first: First value in the sum
    :param second: Second value in the sum
    :param third: Third value to be compared
    :return: True if the sum of the first and second
     are greater than the third
    """

    if first + second > third:
        return True
    else:
        return False
