from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


from django.apps import AppConfig
from threading import Thread

class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        from reminder.reminder import start_scheduler
        scheduler_thread = Thread(target=start_scheduler)
        scheduler_thread.start()
