import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = "Hello,This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library"
sender_address = 'sahiljaindragon123gmail.com'
sender_pass = 'sahiljain0852'
receiver_address = 'jainsahil1116@gmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

message.attach(MIMEText(mail_content, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587) 
session.starttls() 
session.login(sender_address, sender_pass) 
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')