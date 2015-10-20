# Task 2


def main():
    '''
    Asks the user for some input and prints it out, nicely formatted.
    '''
    fname = input("Wie heißt du? ")
    lname = input("Wie ist dein Nachname? ")
    print('Hello {name} {lname}, welcome to \
    Python.'.format(name=fname, lname=lname))


if __name__ == '__main__':
    main()
