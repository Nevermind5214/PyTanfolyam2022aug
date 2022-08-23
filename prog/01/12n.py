import sys


def main():
    if input("Do you really want to quit [y/Y/yes]? ") in ['y', 'Y', 'yes']:
        print('bye')
        sys.exit(0)
    # for any other input:
    print('The show goes on...')

##############################################################################

if __name__ == "__main__":
    main()