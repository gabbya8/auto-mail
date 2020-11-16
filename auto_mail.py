"""
To connect Python to gmail
myaccount.google.com/lesssecureapps
if have 2-factor authentication
myaccount.google.com/apppasswords

 for import os:
 cd ~
 nano .bash_profile
"""
import os
import smtplib
import csv
import pandas as pd
import imghdr
from email.message import EmailMessage

# gets email address and password from computer
# email_address = os.environ.get('email_user')
# email_password = os.environ.get('email_pass')

# email_address = input('Email: ')
# email_password = input('Password: ')
# message = input('Enter message: ')

# returns list of contacts


def process_file(csv_file):
    # reads and parses CSV file
    col_names = ['email']
    file = pd.read_csv(csv_file, names=col_names)
    contacts = file.email.to_list()  # the list of emails
    return contacts


def send_mail(email_address, email_password, contacts, subject, message):
    # sets up email to be sent out
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = contacts

    msg.set_content(message)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    return None


# print(process_file("emails.csv"))
# contacts = []

# while True:
#     if len(contacts) != 0:
#         print ('Contacts so far: ')
#         for name in contacts:
#             print(name)
#     person = input(
#         "Enter an email address, or just hit return to send message: ")
#     if person == "":
#         break
#     try:
#         contacts.append(str(person))
#     except:
#         print("{} is not a string")


# send_mail("gabriellaalexis2399@gmail.com",
#           "Gabbya8*", process_file("emails.csv"), "python email", "This is a test with input")

# reads and parses CSV file
# col_names = ['name', 'email']
# file = pd.read_csv("emails.csv", names=col_names)
# contacts = file.email.to_list() #the list of emails
# print(contacts)

# opens and reads text file with email
# f = open('sample.txt')
# message = f.read()
# f.close()
# print(message)

# for sending images
# if you want to send mult images, you need a list and a loop to go through list

# files = ['../fire.jpg', '../gabby.jpg']

# for file in files:
# 	with open(file, 'rb') as f:
# 		img_file = f.read()
# 		file_type = imghdr.what(f.name)
# 		file_name = f.name

# 	msg.add_attachment(img_file, maintype='image', subtype='file_type', filename='file_name')
