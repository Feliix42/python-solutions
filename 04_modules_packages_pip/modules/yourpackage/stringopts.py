# task 10


def get_length(text):
    return len(text)


def reverse(text):
    return text[::-1]  # or use reversed(text)


def does_include(text, included):
    for character in text:
        if character == included:
            return True

    return False
