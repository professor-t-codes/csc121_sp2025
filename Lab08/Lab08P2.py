#
# Richard Tillies
# December 29, 2024
# Create daily report
#
import sys

def main():
    # Variables, files names, and lists
    categories = []
    totals = []
    line_number = 0
    input_file = 'sales.txt'
    output_file = 'daily_report.txt'

    # Open file for reading
    try:
        file = open(input_file, "r")

        for line in file:
            line_number += 1  # increment line number

            # Split line by comma delimiter
            line_parts = line.strip().split(',')

            # Get amount and category
            try:
                amount = float(line_parts[2].strip())
                category = line_parts[1].strip()

                # If category exists, add amount to running total
                if category in categories:
                    index = categories.index(category)
                    totals[index] += amount

                # If category does not exist, add category and amount to respective lists
                else:
                    categories.append(category)
                    totals.append(amount)

            # Error if amount cannot be converted to float type
            except ValueError:
                print(f'Error on line {line_number}: Could not convert "{line_parts[2].strip()}" to price format')

        # Close reading file
        file.close()

    # Error if read file does not exist
    except FileNotFoundError:
        print(f"File '{input_file}' not found")
        sys.exit()

    # Open file for writing
    file = open(output_file, "w")

    # Write categories and amounts to write file
    for i in range(len(categories)):
        file.write(f'{categories[i]}s: ${totals[i]:,.2f}\n')

    # Write message to console
    print(f'Daily report written to "{output_file}"')

    # Close writing file
    file.close()

# Call main method
main()