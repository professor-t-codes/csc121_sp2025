# Richard Tillies
# January 4, 2025
# ITS Python Certification Review - Problem 3 (os and os.path modules)
#
import os, os.path


def main():
    # display current directory
    show_files_and_dirs()

    # rename file if file exists
    file_old = 'info.txt'
    file_new = 'information.txt'

    if os.path.isfile(file_old):
        os.rename(file_old, file_new)
    else:
        print(f'File {file_old} does not exist. Cannot rename.')

    # create directory if it does not already exist
    dir_name = 'information'

    if os.path.exists(dir_name):
        print(f'Directory {dir_name} already exists. Cannot create.')
    else:
        os.mkdir(dir_name)

    # display current directory
    show_files_and_dirs()


def show_files_and_dirs():
    # star = '* '
    files = os.listdir()
    print('Files and directories in current directory:')
    for file in files:
        if os.path.isdir(file):
            print('\t*', file)
        else:
            print('\t', file)
    print()


# call main method
main()
