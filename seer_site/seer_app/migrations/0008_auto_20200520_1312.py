# Generated by Django 3.0.6 on 2020-05-20 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seer_app', '0007_auto_20200519_1545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='User_Id',
            new_name='User_ID',
        ),
    ]