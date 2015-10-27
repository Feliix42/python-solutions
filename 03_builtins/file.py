# task 6


def step1():
    '''
    Writes a string to a file.
    Always remember to close the file handle.
    You can check the results by opening the file with any text editor.
    '''
    file = open('myfile.txt', 'w')
    file.write("hello")
    file.close()


def step2():
    '''
    Opens the loremipsum file from the "res" directory and
    prints the file, line by line, to the console.
    The `for` loop comes in handy for this.
    '''
    with open('res/loremipsum.txt', 'r') as myfile:
        # iterate over the lines of the file
        for line in myfile:
            print(line)


def step3():
    '''
    Reads the content of a file and writes it back.
    Since this requires two file openings and closings, we need to save the
    lines of the file in a separate variable (here called `backup`)
    '''
    backup = []     # because of scoping
    with open('res/loremipsum.txt', 'r') as f:
        backup = f.readlines()
        # f.readlines() returns a list of lines
        # alternatively you can use f.read() which gives you the whole content as string
    with open('res/loremipsum.txt', 'w') as f:
        for line in backup:
            f.write(line)


def step4():
    '''
    Appends a line of text to the `lorem ipsum` file.
    We use the context manager for this example.
    '''
    with open('res/loremipsum.txt', 'a') as myfile:
        myfile.write('Warum ist es immer "Lorem Ipsum..."?')


def main():
    step1()
    step2()
    step3()
    step4()

if __name__ == '__main__':
    main()
