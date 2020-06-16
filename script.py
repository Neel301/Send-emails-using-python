import pandas as pd
import smtplib

SenderAddress = "<Email Address of sender>"
password = "password of sender"

e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("MY_EMAIL", "MY_PASS")
msg = "Welcome to Germany"
subject = "Hello"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail("MY_EMAIL", email, body)
server.quit()
