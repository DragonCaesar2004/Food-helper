import ssl
import smtplib
from email.message import EmailMessage
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
import atexit
from main.utils import get_user_emails
import os
from dotenv import load_dotenv
load_dotenv()
email_sender = "foodhelperproject@gmail.com"
email_password = os.getenv('EMAIL_HOST_PASSWORD')
email_subject = "Не забудьте правильно питаться!"
email_text = 'http://127.0.0.1:8000/'
context = ssl.create_default_context()

def reminder():
    for email_receiver in get_user_emails():
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = email_subject
        em.set_content(email_text)
        
        with smtplib.SMTP_SSL('smtp.gmail.com', port=465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f"Email sent successfully to {email_receiver}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        reminder,
        trigger=CronTrigger(hour=2, minute=36),  # Запуск каждый день в 01:30
        id='daily_reminder',
        name='Daily Reminder Email',
        replace_existing=True,
    )
    scheduler.start()
    logging.info("Scheduler started")

    # Обработка завершения работы для корректного завершения планировщика
    atexit.register(lambda: scheduler.shutdown())
