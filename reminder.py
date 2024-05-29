import schedule
import time
import ssl
import smtplib

from email.message import EmailMessage

email_sender = "foodhelperproject@gmail.com"
email_password = "omep qscs vvaq ifwn"
email_receiver = "theartemartemka@gmail.com"

email_subject = "Не забудьте правильно питаться!"

email_text = 'http://127.0.0.1:8000/'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_subject
em.set_content(email_text)
context = ssl.create_default_context()



def reminder():
    with smtplib.SMTP_SSL('smtp.gmail.com', port = 465, context = context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    


schedule.every().day.at("08:00").do(reminder)

while True:
    schedule.run_pending()
    time.sleep(1)