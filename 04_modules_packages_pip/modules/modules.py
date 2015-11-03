# task 10

from yourpackage import basicmath
from yourpackage import stringopts

'''
If you are in step 1 just import basicmath
'''


def main():
    print(basicmath.add(2, 5))
    print(basicmath.multiply(3, 5))
    # ...

    # stringopts:
    print(stringopts.get_length('Hello'))
    print(stringopts.reverse('Hello'))
    print(stringopts.does_include('Hello', 'a'))
    print(stringopts.does_include('Hello', 'e'))

if __name__ == '__main__':
    main()
