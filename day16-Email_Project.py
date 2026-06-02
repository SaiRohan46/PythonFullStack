'''
SMTP(Simple Mail Transfer Protocol)
-----------------------------------
--> this is used to send mails from server to another...
Note:
-----
1.SMTP SSL Port
----------------
465

2.SMTP TLS Port
----------------
587

import smtplib

EmailMessage Class
-----------------
msg['Subject'] = 'SMTP ON Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Reciever@mail.com'



import smtplib
from email.message import EmailMessage
sender = 'rohansai4645@gmail.com'
password = 'mjbvkjzlabswohur'
msg = EmailMessage()
msg['Subject'] = 'Welcome Mail'
msg['From'] = sender
msg['To'] = 'kavs14345@gmail.com'
msg.set_content('Your Account has been credited with Rs.75,000')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''
import smtplib
from email.message import EmailMessage
sender = 'rohansai4645@gmail.com'
password = 'hrjizqezkvgbjfrg'
receiver = ['kavs14345@gmail.com','chaitanyakumartoi2004@gmail.com','karthikyedagiri@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    msg=EmailMessage()
    msg['Subject'] = 'Welcome Mail'
    msg['From'] = sender
    msg['To'] = email
    msg.set_content('Your Instagram is Not Hacked🤣')
    server.send_message(msg)
server.quit()






