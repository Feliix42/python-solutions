# task 18

import time
import urllib.request
import json


def buildlink():
    '''
    Step one: Build the link for todays meals.
    '''
    today = time.strftime("%Y-%m-%d")
    link = 'http://openmensa.org/api/v2/canteens/{mensa}/days/{date}/meals'.format(
        mensa=79, date=today)
    return link


def readurl(url):
    '''
    This will open our URL and read the contents from the page.
    Then, everything will be parsed using the json module.
    '''
    ret = urllib.request.urlopen(url)
    meals = json.loads(ret.read().decode("UTF-8"))
    # print(json.dumps(meals, indent=4))
    return meals


def printmeals(meals):
    '''
    Takes a list of dicts from the OpenMensa API and prints every
    meal with some more information.
    '''
    for meal in meals:
        if meal["prices"]["students"] == None:
            preis = 'unbekannt viel'
        else:
            preis = str(meal["prices"]["students"]) + ' €'
        print(meal['name'])
        print('    Dieses Essen kostet: {geld}\n'.format(geld=preis))


def main():
    # get the latest link
    link = buildlink()
    # print(link)   # prints the link built by buildlink()
    meals = readurl(link)
    # print the meals in a nice format
    printmeals(meals)


if __name__ == '__main__':
    main()
