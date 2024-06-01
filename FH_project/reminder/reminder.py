import ssl
import smtplib
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from email.message import EmailMessage
import logging
import atexit

email_sender = "foodhelperproject@gmail.com"
email_password = "omep qscs vvaq ifwn"
email_receiver = "tmrgmdv2004@gmail.com"

email_subject = "Не забудьте правильно питаться!"
email_text = 'http://127.0.0.1:8000/'

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = email_subject
em.set_content(email_text)
context = ssl.create_default_context()

def reminder():
    with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    #print("Email sent successfully")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        reminder,
        trigger=CronTrigger(hour=2, minute=4),  # Запуск каждый день в 01:30
        id='daily_reminder',
        name='Daily Reminder Email',
        replace_existing=True,
    )
    scheduler.start()
    logging.info("Scheduler started")

    # Обработка завершения работы для корректного завершения планировщика
    atexit.register(lambda: scheduler.shutdown())
