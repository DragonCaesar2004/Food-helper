# Generated by Django 4.2.13 on 2024-05-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='allergies',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='goal',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='vegan_vegetarian',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]