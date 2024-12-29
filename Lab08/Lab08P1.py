#
# Richard Tillies
# December 29, 2024
# Read from text file
#

# Lists for labels and counters
labels = ["CRITICAL", "ERROR", "WARNING", "INFO", "UNKNOWN"]
counters = [0, 0, 0, 0, 0]

# Open file for reading
try:
    file = open("program.log", "r")

    # Split line by space delimiter
    for line in file:
        line_parts = line.strip().split(' ')

        # Identify the error category and increment the corresponding counter
        # If error not in list, increment unknown counter
        try:
            index = labels.index(line_parts[3])
            counters[index] += 1
        except ValueError:
            counters[4] += 1

    # Display each error category and counter
    for i in range(len(counters)):
        print(f'{labels[i]}: {counters[i]}')

    # Close reading file
    file.close()

# Error if file does not exist
except FileNotFoundError:
    print('File does not exist')
