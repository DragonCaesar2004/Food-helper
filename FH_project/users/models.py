from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    goal = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    vegan_vegetarian = models.CharField(max_length=15)
    allergies = models.TextField(blank=True)
    weight = models.FloatField()
    height = models.FloatField()


from django.db import models

class Meal(models.Model):
    user_id = models.IntegerField()  # Идентификатор пользователя
    type = models.CharField(max_length=100)  # Тип приема пищи (например, завтрак, обед, ужин)
    time = models.TimeField()  # Время (часы:минуты)
    rating = models.PositiveSmallIntegerField()  # Оценка от 0 до 10
    name = models.CharField(max_length=200)  # Название 
    quantity = models.IntegerField()  # Количество
    quantity_type = models.CharField(max_length=100)  # Тип количества (например, граммы, миллилитры)
    date_added = models.DateTimeField(auto_now_add=True)  # Дата добавления (время дата)

    def __str__(self):
        return f"{self.type} - {self.name}"

# После добавления этой модели в models.py вашего приложения, выполните следующие команды:
# python manage.py makemigrations
# python manage.py migrate
