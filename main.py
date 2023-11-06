#imports
import os
import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

emails = []

#Fuction to GetContacts
def get_contacts(filename):
  with open(filename, mode='r', encoding='utf-8') as contacts_file:
      for a_contact in contacts_file:
        emails.extend(a_contact.split())
  return emails

#Fuction to send email
def enviar_email():
  n = 0
  for email in emails:
    
    corpo = """Your text goes here"""""
    msg = MIMEMultipart()
    msg['Subject'] = '' #Subejct
    msg['From'] = '' #Your email
    msg['To'] = emails[n] #contacts list
    password = '' #app password gmail
    msg.add_header('Content-Type', 'text/html')
    msg.attach(MIMEText(corpo))
  
    
  
    pdf_file = 'myarchive.pdf' #name of pdf file
    attachment = open(pdf_file, 'rb') 
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)
  
    att.add_header('Content-Disposition', 'attachment', filename='name to file in email')
    attachment.close()
    msg.attach(att)
  
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    n=n+1
    print('Email send')

#execution
confirmation = input("Type 'Start' to start the script: ")
confirmation.lower()
if confirmation == 'start': #confirmation to start script, you can remove this for more velocity
  get_contacts('contacts.txt') #get contacts from file by the name of file.
  enviar_email() #send emails
else:
  print('Script stopped')
