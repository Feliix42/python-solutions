# Task 4

'''
This task was meant to be done in the interpreter.
'''


class A():
    # an empty class
    pass


class B():
    def my_method(self):
        return 42


class C():
    gender = 'male'

    def __init__(self, name, age):
        self.name = name
        self.age = age


class D():
    def __init__(self, number):
        self.value = number

    def plus(self):
        return self.value + 3


def main():
    # Step 1
    # create a new instance of the class A
    a = A()

    # Let's add the two attributes and print them to make sure they exist
    a.id_string = 'id#456'
    a.id_value = 456
    print(a.id_string)
    print(a.id_value)

    # Step 2
    b = A()
    # see the hint on the Exercise page to see what happens when you try
    # to access id_value or id_string

    # Step 3
    c = B()
    print(c.my_method())
    print(B.my_method(c))

    # Step 4
    d = C('John', 42)
    e = C('Jane', 30)
    print(d.name)
    print(e.age)

    # Step 5
    print(d.gender)
    print(e.gender)
    # change the class attribute for one object
    e.gender = 'female'
    # check the values of the attribute 'gender' again
    print(d.gender)
    print(e.gender)

    # Step 6
    num1 = D(8)
    num2 = D(12)
    print(num1.plus())
    print(num2.plus())


if __name__ == '__main__':
    main()
