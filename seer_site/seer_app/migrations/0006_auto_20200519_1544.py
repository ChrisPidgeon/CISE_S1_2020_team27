# Generated by Django 3.0.6 on 2020-05-19 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seer_app', '0005_auto_20200519_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Publication_date',
            field=models.DateField(default=datetime.date(2020, 5, 19), verbose_name='Publication Date'),
        ),
        migrations.AddField(
            model_name='user',
            name='Birth_date',
            field=models.DateField(default=datetime.date(2020, 5, 19), verbose_name='Birth Date'),
        ),
    ]