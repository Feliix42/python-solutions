# task 19

import re
import json
import urllib.request


def get_data():
    # STEP 1
    # Get the Json from the URL

    data = urllib.request.urlopen('http://fsr.github.io/\
python-lessons/misc/christmas.json')
    wishlist = json.loads(data.read().decode('utf-8'))
    return wishlist


def do_santas_work(wishlist):

    # STEP 2
    # Sort out the Spam
    no_spam = re.compile(r'^Lieber Weihnachtsmann,')
    nice = {}
    naughty = []

    for child in wishlist:
        if no_spam.match(wishlist[child]):

            # STEP 3
            # If no spam check if child was nice
            if nice_or_not(wishlist[child]):

                # STEP 4
                # Get the wishes
                nice[child] = get_wishes(wishlist[child])
            else:
                naughty.append(child)
        else:
            naughty.append(child)
    nice['naughty'] = naughty

    return nice


def nice_or_not(letter):
    # Check if child was nice
    nice = re.compile(r'immer (lieb)|(artig)|(brav)')
    if nice.search(letter) is not None:
        return True
    else:
        return False


def get_wishes(letter):
    # Get all wishes out of the letter
    wish_pattern = re.compile(r'- (.*)')

    wishes = wish_pattern.finditer(letter)
    wishlist = []

    for wish in wishes:
        wishlist.append(wish.group(1))

    return wishlist


def show_santa(results):

    # STEP 5
    # Finally present results to Santa
    for child in results['naughty']:
        print('{child}: unartig/keine Wünsche'.format(child=child))

    del results['naughty']

    for child in results:
        print('{child}: {whishes}'.format(child=child,
                                          whishes=', '.join(results[child])))


def main():
    wishlist = get_data()
    results = do_santas_work(wishlist)
    show_santa(results)

if __name__ == '__main__':
    main()
