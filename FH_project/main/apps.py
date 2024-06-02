from django.apps import AppConfig
from threading import Lock

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scheduler_started = False
        self.scheduler_lock = Lock()

    def ready(self):
        with self.scheduler_lock:
            if not self.scheduler_started:
                self.scheduler_started = True
                from reminder.reminder import start_scheduler
                start_scheduler()
