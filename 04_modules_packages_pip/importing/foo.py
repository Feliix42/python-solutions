# task 9

import bar

'''
If you try step 3 of that task you have to use the following lines before you
import bar

import sys

sys.path.append(’path/to/directory’)
'''


def main():
    print(bar.MY_CONST)
    print(bar.calculate(4, 13))


if __name__ == '__main__':
    main()
