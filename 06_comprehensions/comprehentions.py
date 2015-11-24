# task 13

list1 = [i for i in range(1, 10)]
print(list1)

text = ''
with open('resources/lorem') as file:
    text = file.read()


list2 = [len(word) for word in text.split()]
print(list2)


# the function that creates tuples
def function(l1, l2):
    maxlen = len(l1) if len(l1) < len(l2) else len(l2)
    return [(l1[index], l2[index]) for index in range(maxlen)]

    '''
    this could be done easier with
    return zip(l1, l2)
    '''

print(function(text.split(), list2))

# dict (part 2)

dictcomp = {key: len(key) for key in text.split()}
print(dictcomp)


# generator (part 3)
tuplegen = dict((key, len(key)) for key in text.split())
print(tuplegen)
