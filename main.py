import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

print("Welcome to Email Marketing")
# This can be read from a csv
emailList = ['21f1002538@student.onlinedegree.iitm.ac.in', 'rishabh22211@gmail.com', 'rishabh11336@gmail.com']

def sendMail(fromEmail, toEmail, subject, message):
  msg = MIMEMultipart()
  msg.set_unixfrom("rishabh")
  msg['From'] = fromEmail
  msg['To'] = toEmail
  msg['Subject'] = subject
  msg.attach(MIMEText(message))
  mailserver = smtplib.SMTP('smtp.gmail.com', 587)
  mailserver.ehlo()
  mailserver.starttls()
  mailserver.login(fromEmail, os.environ['password']) 
  
  mailserver.sendmail(fromEmail, toEmail, msg.as_string())
  mailserver.quit()
  
for email in emailList: 
  fromEmail = "ecomdjango@gmail.com"
  subject = "Jeene mera dil luteya"
  message = "Ohooo"
  sendMail(fromEmail, email, subject, message)
  print(f"Mail sent to - {email}")
  time.sleep(2)

print("All emails sent successfully")

