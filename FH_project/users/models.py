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