# Generated by Django 3.0.6 on 2020-06-01 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seer_app', '0009_auto_20200601_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='accountroles',
            options={'verbose_name': 'Account Role', 'verbose_name_plural': 'Account Roles'},
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='search',
            options={'verbose_name_plural': 'Searches'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.RemoveField(
            model_name='roles',
            name='Role_Description',
        ),
        migrations.AddField(
            model_name='roles',
            name='Role_Type',
            field=models.CharField(choices=[('ROLE_S', 'Submitter'), ('ROLE_M', 'Moderator'), ('ROLE_A', 'Analyst'), ('ROLE_G', 'General User')], default='ROLE_G', max_length=6),
        ),
    ]
