import sys


def lame_function(num1, num2):
    # this is a simple function
    return num1 * num2


def add_all(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def main():
    # rename the simple function and use it
    fancy_new_func = lame_function
    print(fancy_new_func(2, 5))

    # test the functionality of add_all()
    print(add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

    # get all arguments to the script, remove filename
    args = sys.argv
    args.remove(__file__)

    # cast all arguments to int, catch ValueErrors
    try:
        # note that we use a Comprehension here and assign the list back
        # to it's old identifier
        args = [int(x) for x in args]
    except ValueError:
        print("Please only Integers here!")
    else:
        # unpack the args list and call add_all() with those arguments
        print(add_all(*args))

    # lambda function part
    print((lambda x, y: x*y)(2, 3))


if __name__ == '__main__':
    main()
