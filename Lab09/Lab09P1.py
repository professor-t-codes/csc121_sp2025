#
# Richard Tillies
# December 29, 2024
# Word counting in dictionaries
#

# DO NOT UPDATE ANY PART OF THE MAIN FUNCTION
def main():
    input_file = open('words.txt', 'r')  # Open a file for reading
    file_text = input_file.read().upper()  # Read all contents and convert to uppercase
    process_file(file_text)
    input_file.close()


def process_file(text):
    """
    This function creates a dictionary of words and their counts from the input text.
    It then identifies the words that appear the most in the dictionary, displays
    those words (with their count), and then removes them from the dictionary.
    Finally, it extracts and sorts the remaining words as a list and displays it.

    :param text: Text string to be parsed into a dictionary
    :return:
    """

    # TODO: Create an empty dictionary
    word_dict = {}

    # TODO: Use the split method to get a list of words from the input parameter
    word_list = text.split()
    print(word_list)

    # TODO: Use a for loop to go through the list 1-by-1
    #  and count the occurrence of each word. Add or update
    #  the entries in the dictionary with the word/count pairs.
    max_count = 0
    for word in word_list:
        if word_dict.__contains__(word):
            word_dict[word] += 1
        else:
            word_dict[word] = 1

        if word_dict[word] > max_count:
            max_count = word_dict[word]

    # TODO: Print the dictionary
    print(word_dict)

    # TODO: Create a list of words with the maximum count
    #  and print the list.
    max_list = []
    for word in word_dict:
        if word_dict[word] == max_count:
            max_list.append(word)

    print(f'Words with max count of {max_count}: {max_list}')
    # TODO: Remove the words with max count from the dictionary
    #  and print the dictionary.
    for word in max_list:
        # print(word)
        word_dict.pop(word)

    print(f'Dictionary with max removed: {word_dict}')

    # TODO: Put all the words in the dictionary in a list, sort it,
    #  and print the list of sorted words.
    sorted_list = list(word_dict.keys())
    sorted_list.sort()
    print(f'Words sorted: {sorted_list}')

    # pass  # TODO: Remove this line before submitting to BB.


main()
