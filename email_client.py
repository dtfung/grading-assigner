# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 22:50:30 2017

@author: donal
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

USER_EMAIL = None
PASSWORD = None
RECIPIENT = None
MSG_BODY = None

def send_email(user_email, password, recipient, msg_body):

    fromaddr = user_email
    toaddr = recipient
    body = msg_body
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "New Submission Received!!!"
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("Successfully sent email")
    except:
        print("Error: unable to send email")
       
if __name__ == "__main__":
    
    send_email(user_email = USER_EMAIL,
                 password = PASSWORD,
                 recipient = RECIPIENT,
                 msg_body = MSG_BODY)