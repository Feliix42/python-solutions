#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText


def buildmessage():

    # The MIMEText Object alsways will be created with the message content
    message = MIMEText('Text der E-Mail.')

    # set the sender of your mail
    message['From'] = 'Sender name <sender@example.com>'
    # set the receiver of your mail
    message['To'] = 'Receiver name <receiver@example.com>'

    # set the subject of you mail
    message['Subject'] = 'Betreff der E-Mail'

    return message


def main():

    # building the message
    message = buildmessage()

    # Set the basic variables for the SMTP server
    server = 'Servername'
    port = 587  # This is the default Port of an smtp server

    # We want to use a try except here for any error from smtplib
    try:
        # establishing a connection to the host (with a filehandler)
        with smtplib.SMTP(host=server, port=port) as smtpObj:
            # make the connection secure
            smtpObj.starttls()
            
            smtpObj.login('user', 'pass')
            smtpObj.send_message(message)
    except smtplib.SMTPException as error:
        print("Error: unable to send email because of the following reason:\
\n {}".format(error))

if __name__ == '__main__':
    main()
