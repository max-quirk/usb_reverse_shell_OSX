from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys
import os

os.chdir("../../")

msg = MIMEMultipart()
 
part = MIMEText("Hi, please find the attached file")

msg.attach(part)
 
part = MIMEApplication(open(str(sys.argv[1]),"rb").read())

part.add_header('Content-Disposition', 'attachment', filename=str(sys.argv[1]))

msg.attach(part)
 
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login("SENDING EMAIL", "PASSWORD")
server.sendmail("SENDING EMAIL", "RECEIVING EMAIL", msg.as_string())
server.close()

print('Sent')
