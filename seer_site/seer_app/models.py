import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class User(models.Model):
    User_ID = models.IntegerField(max_length = 4, primary_key =True)
    F_name = models.CharField(max_length = 40)
    L_name = models.CharField(max_length = 40)
    Birth_date = models.DateTimeField
    Email = models.CharField(max_length = 80)

class Account(models.Model):
    Account_ID = models.IntegerField(max_length = 4, primary_key = True)
    User_Id = models.ForeignKey()
    Username = models.CharField(max_length = 40)
    Password = models.CharField(max_length = 40)

class AccountRoles(models.Model):
    Account_ID = models.ForeignKey()
    Role_ID = models.ForeignKey()

class Roles(models.Model):
    Role_ID = models.IntegerField(max_length = 4, primary_key = True)
    Role_Description = models.CharField(max_length = 40)
    ####integrate an enum here

class Search(models.Model):
    Search_ID = models.IntegerField(max_length = 4, primary_key = True)
    Keywords = models.CharField(max_length = 50)
    User_ID = models.ForeignKey()
    Article_ID = models.ForeignKey()

class Article(models.Model):
    Article_ID = models.IntegerField(max_length = 4,primary_key = True)
    Title = models.CharField(max_length = 100)
    Author = models.CharField(max_length = 100)
    Publication_date = models.DateTimeField
    Journal = models.CharField(max_length = 200)
    Volume = models.IntegerField(max_length = 3)
    Issue = models.IntegerField(max_length = 3)
    Article_Description = models.TextField(max_length = 800)
    User_ID = models.ForeignKey()
    ###Status Integrate an enum here
