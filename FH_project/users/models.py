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

class Food(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    name_of_food = models.TextField()
    quantity = models.FloatField()
    # evaluation = models.TextField(null=True, blank=True)
    description = models.TextField()