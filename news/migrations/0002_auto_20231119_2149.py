# Generated by Django 3.2 on 2023-11-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafeteria',
            name='cafeteria_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servedtime',
            name='served_time_period',
            field=models.CharField(max_length=100),
        ),
    ]
