# Task 3


inputText = input('Your Text here: ')

if inputText.isupper():
    '''
    This tests the String if it is uppercase
    '''
    print('IS UPPERCASE')
    '''
    This is the extention of Step 2
    '''
    print('Here is a lower version:')
    print(inputText.lower())
elif inputText.isnumeric():
    '''
    This tests the String if it is numeric
    '''
    print('15 num3r1c')
    '''
    This is the extention of Step 2
    '''
    secondNumber = input('Type in a second number, please: ')
    print('The sum of {one} + {two} is {sum}'.format(one=int(inputText),
                                                     two=int(secondNumber),
                                                     sum=int(inputText) + int(secondNumber)))
elif ':-)' in inputText:
    print('It contains a smile :-)')
else:
    print('Oh no, it is nothing!')
    textList = inputText.split('a')
    print(';'.join(textList))
