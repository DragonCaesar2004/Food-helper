from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import atexit
from .sender import send_to_rabbitmq
from .receive import get_elems

def start_scheduler():
    scheduler = BackgroundScheduler()

    # Добавляем первую задачу
    scheduler.add_job(
        send_to_rabbitmq,
        trigger=CronTrigger(hour=13, minute=40),   
        id='daily_reminder',
        name='Daily Reminder Email',
        replace_existing=True,
    )

    # Добавляем вторую задачу
    scheduler.add_job(
        get_elems,
        trigger=CronTrigger(hour=13, minute=42),   
        id='get_elements',
        name='Get Elements from Q',
        replace_existing=True,
    )

    scheduler.start()
 
    # Обработка завершения работы для корректного завершения планировщика
    atexit.register(lambda: scheduler.shutdown())
