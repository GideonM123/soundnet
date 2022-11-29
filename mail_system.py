#Goal: Create script to send an email
#Requirements: -Use SMTP
#              -Sends email to whatever email-address you give it

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()
server.starttls()
server.login('x@gmail.com','x')

msg = MIMEMultipart()
msg['From'] = 'x@gmail.com'
msg['To '] = 'x@gmail.com'
msg['Subject'] = 'Test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

text = msg.as_string()
server.sendmail('x@gmail.com','x@gmail.com',text)













