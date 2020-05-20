# Generated by Django 3.0.6 on 2020-05-18 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('Account_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('Article_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
                ('Journal', models.CharField(max_length=200)),
                ('Volume', models.IntegerField(max_length=3)),
                ('Issue', models.IntegerField(max_length=3)),
                ('Article_Description', models.TextField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('Role_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Role_Description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=40)),
                ('L_name', models.CharField(max_length=40)),
                ('Email', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('Search_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Keywords', models.CharField(max_length=50)),
                ('Article_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seer_app.Article')),
                ('User_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seer_app.User')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='User_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seer_app.User'),
        ),
        migrations.CreateModel(
            name='AccountRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seer_app.Account')),
                ('Role_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seer_app.Roles')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='User_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seer_app.User'),
        ),
    ]
