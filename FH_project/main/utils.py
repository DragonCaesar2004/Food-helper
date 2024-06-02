# utils.py или в соответствующем месте вашего приложения
from django.db import connection
from users.models import CustomUser

 

def get_user_emails():
    for user in CustomUser.objects.values_list('email', flat=True).iterator():
        yield user
