##
# Richard Tillies
# December 20, 2024
# Process IP addresses
##

def get_input():
    return input("Please enter an IP address or 'Q' to quit: ")

def main():
    user_input = get_input()

    while user_input.lower() != 'q':
        ip_parts = user_input.split('.')
        if len(ip_parts) != 4:
            print('Error: An IP address should consist of 4 parts separated by periods.')
        else:
            error_flag = False
            for part in ip_parts:
                try:
                    number = int(part)
                    if number < 0 or number > 255:
                        print(f'Error with {number}: Each part of the IP address should be a number between 0 and 255.')
                        error_flag = True
                        break
                except ValueError:
                    print(f'Error with {part}: Each part of the IP address should be a number between 0 and 255.')
                    error_flag = True
                    break

            if not error_flag:
                print(user_input.replace('.',':'))

        user_input = input("Please enter an IP address or 'Q' to quit: ")

    # print('Done')

# Call main function
main()