#
# Richard Tillies
# December 20, 2024
# Using matplotlib module to create a bar graph
#
import matplotlib.pyplot as plt

def main():
    # Get title and axis labels
    title = input('Enter the bar graph title: ')
    xlabel = input('Enter the label for the x-axis: ')
    ylabel = input('Enter the label for the y-axis: ')

    # Get number of data points
    count = int(input('Enter the number of data points: '))

    # Get the name and value of each tick
    names = []
    values = []
    for tick in range(count):
        name = input(f'Enter the name for tick {tick+1}: ')
        value = float(input(f'Enter the value for tick {tick+1}: '))
        names.append(name)
        values.append(value)

    # Create the bar graph
    plt.bar(names, values)

    # Add the chart title
    plt.title(title)

    # Add labels for x-axis and y-axis
    plt.xlabel = xlabel
    plt.ylabel = ylabel

    # Display bar graph
    plt.show()

# Call main function
main()