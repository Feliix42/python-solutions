import json
import random
import os


# global dict for all humans
humans = {}


def loadlist():
    '''
    Loads the raw contact data from the given JSON file.
    '''
    with open('res/contactdata.json') as listfile:
        contactdata = json.load(listfile)
    return contactdata


def gen_contacts(cycles=1):
    '''
    Genreates a number of contacts (1 by default) and
    adds them to the humans dict.
    '''
    contactnames = loadlist()

    # initialize the random generator
    random.seed()
    for count in range(cycles):
        # get a random index from the list of first/last names
        i = random.randint(0, len(contactnames["firstnames"]) - 1)
        j = random.randint(0, len(contactnames["lastnames"]) - 1)

        # generate the false contact data
        name = contactnames["firstnames"][i] + ' ' + contactnames["lastnames"][j]
        mail = contactnames["firstnames"][i] + '.' + contactnames["lastnames"][j] + '@python.course'
        phone = random.randint(100000000000, 999999999999)
        dob = '01.01.1859'

        # add the human to the humans dict
        humans[name] = {'name': name, 'dob': dob, 'phone': phone, 'mail': mail}


def main():
    global humans
    # check if there is already a json file with contacts
    if os.path.exists('contacts.json'):
        with open('contacts.json') as f:
            humans = json.load(f)
        gen_contacts(3)
    else:
        gen_contacts(20)

    # dump the contacts back to the JSON file
    with open('contacts.json', 'w') as f:
        json.dump(humans, f, indent=4)


if __name__ == '__main__':
    main()
