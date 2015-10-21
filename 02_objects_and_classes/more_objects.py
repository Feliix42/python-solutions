# Task 5


# an empty list, that is globally defined -> for storing your contacts
contacts = []


class Contact:
    '''
    A class for managing a contact.
    '''
    def __init__(self, name, dateofbirth, phone, mail):
        '''
        Creates a new instance of the class 'Contact' (creates a new contact).
        This function takes a name, the date of birth of the contact,
        phone number and mail address.
        '''
        self.name = name
        self.dob = dateofbirth
        self.phone = phone
        self.mail = mail

    def __str__(self):
        '''
        String representation of the contact.
        NOTE: '\n' is a line break
        '''
        return "Contacts of {name}, born on {dob}:\n \
Phone: {phone}\n Mail: {mail}".format(name=self.name, dob=self.dob,
                                      phone=self.phone, mail=self.mail)

    def change_mail(self, newmail):
        '''
        Changes the mail address of a contact.
        '''
        self.mail = newmail

    def change_phone(self, newnum):
        '''
        Changes the phone number of a contact
        '''
        self.phone = newnum

    def spliced_mail(self):
        '''
        The interactive version of changing the mail address of a contact.
        Takes the new address as input and changes the address (this can
        also be done by using the change_mail() function).
        Works similar for changing the phone number interactively
        '''
        newmail = input("What is the new Mail address for {person}? (old: {old})\
 ".format(person=self.name, old=self.mail))
        self.mail = newmail

    def spliced_phone(self):
        newphone = input("What is the new Phone nummber for {person}? (old: {old})\
 ".format(person=self.name, old=self.phone))
        self.phone = newphone


def main():
    # add some contacts and add them to the contact list
    batman = Contact("Batman", "23. July 1939", "0123/456789",
                     "nanananananananananananananananan@batman.com")
    contacts.append(batman)
    print(batman)
    matthias = Contact("Matthias Stuhlbein", "28. Feb 2015", "000000000000",
                       "matthias@theonlyone.de")
    contacts.append(matthias)

    # call the spliced 'change mail' dialogue and verify that the address changed
    matthias.spliced_mail()
    print(matthias)


if __name__ == '__main__':
    main()
