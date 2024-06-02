import ssl
import smtplib
from email.message import EmailMessage
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
#import logging
import atexit
from main.utils import get_user_emails
from .sender import send_to_rabbitmq




def start_scheduler():
    print('first')

    scheduler = BackgroundScheduler()
    scheduler.add_job(
        send_to_rabbitmq,
        trigger=CronTrigger(hour=4, minute=5),  # Запуск каждый день в 01:30
        id='daily_reminder',
        name='Daily Reminder Email',
        replace_existing=True,
    )
    scheduler.start()
    #logging.info("Scheduler started")context=context

    # Обработка завершения работы для корректного завершения планировщика
    atexit.register(lambda: scheduler.shutdown())

from .receive import get_elems
def get_elements_from_q():
    print('second')
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        get_elems,
        trigger=CronTrigger(hour=4, minute=11),  # Запуск каждый день в 01:30
        id='daily_reminder',
        name='Daily Reminder Email',
        replace_existing=True,
    )
    scheduler.start()
    #logging.info("Scheduler started")

    # Обработка завершения работы для корректного завершения планировщика
    atexit.register(lambda: scheduler.shutdown())