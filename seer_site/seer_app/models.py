import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    User_ID = models.IntegerField(primary_key = True)
    F_name = models.CharField(max_length = 40)
    L_name = models.CharField(max_length = 40)
    Birth_date = models.DateTimeField
    Email = models.CharField(max_length = 80)
    def __str__(self):
        return "Name: {} {}/nBirth Date: {}/nEmail: {}/n".format(self.F_name, self.L_name, self.Birth_date, self.Email)
    
class Account(models.Model):
    Account_ID = models.IntegerField(primary_key = True)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Username = models.CharField(max_length = 40)
    Password = models.CharField(max_length = 40)
    def _str_(self):
        return "Account ID: {}/nUsername: {}/n".format(self.Account_ID, self.Username)

class Roles(models.Model):
    Role_ID = models.IntegerField(primary_key = True)
    Role_Description = models.CharField(max_length = 40)
    def _str_(self):
        return "Role: {}/n".format(self.Role_Description)

class AccountRoles(models.Model):
    Account_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
    Role_ID = models.ForeignKey(Roles, on_delete=models.CASCADE)

class Article(models.Model):
    Article_ID = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length = 100)
    Author = models.CharField(max_length = 100)
    Publication_date = models.DateTimeField
    Journal = models.CharField(max_length = 200)
    Volume = models.IntegerField()
    Issue = models.IntegerField()
    Article_Description = models.TextField(max_length = 800)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    ###Status Integrate an enum here
    def _str_(self):
        return self.Article_Description

class Search(models.Model):
    Search_ID = models.IntegerField(primary_key = True)
    Keywords = models.CharField(max_length = 100)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Article_ID = models.ForeignKey(Article, on_delete=models.CASCADE)
    def _str_(self):
        return "Search ID: {}/nKeywords: {}/n".format(self.Search_ID, self.Keywords)