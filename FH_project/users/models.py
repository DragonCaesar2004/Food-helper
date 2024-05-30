from django.contrib.auth.models import AbstractUser
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

class Meal(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meal_type = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField(auto_now_add=True)
    name_of_food = models.CharField(max_length=255)
    quantity = models.FloatField()
    evaluation = models.IntegerField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)