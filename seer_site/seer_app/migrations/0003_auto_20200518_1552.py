# Generated by Django 3.0.6 on 2020-05-18 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seer_app', '0002_auto_20200518_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Issue',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='Volume',
            field=models.IntegerField(),
        ),
    ]