import datetime

from django.db import models
from django.utils import timezone
from enum import Enum
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(models.Model):
    User_ID = models.AutoField(primary_key = True)
    F_name = models.CharField(max_length = 40, default = '', null = False)
    L_name = models.CharField(max_length = 40, default = '', null = False)
    Birth_date = models.DateTimeField
    Email = models.CharField(max_length = 80, default = '', null = False)
    def __str__(self):
        return "Name: {} {}/nBirth Date: {}/nEmail: {}/n".format(self.F_name, self.L_name, self.Birth_date, self.Email)

class Account(models.Model):
    Account_ID = models.AutoField(primary_key = True)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE)
    Username = models.CharField(max_length = 40, default = '', null = False)
    Password = models.CharField(max_length = 40, default = '', null = False)
    def _str_(self):
        return "Account ID: {}/nUsername: {}/n".format(self.Account_ID, self.Username)

class Roles(models.Model):
    Role_ID = models.AutoField(primary_key = True)
    Role_Description = models.CharField(max_length = 40, default = '', null = False)
    def _str_(self):
        return "Role: {}/n".format(self.Role_Description)

class AccountRoles(models.Model):
    Account_ID = models.ForeignKey(Account, on_delete=models.CASCADE)
    Role_ID = models.ForeignKey(Roles, on_delete=models.CASCADE)
    def _str_(self):
        return "Account ID: {}/nRole ID: {}/n".format(self.Account_ID, self.Role_ID)

class Article(models.Model):
    class ArticleStatus(models.TextChoices):
        SUBMITTED = 'SUB', _('SUBMITTED')
        IN_MODERATION = 'IN_MOD', _('IN MODERATION')
        MODERATED = 'MOD', _('MODERATED')
        ANALYZED = 'ANA', _('ANALYZED')
        SAVED = 'SAV', _('SAVED')
    Article_ID = models.AutoField(primary_key = True)
    Title = models.CharField(max_length = 100, default = '', null = False)
    Author = models.CharField(max_length = 100, default = '', null = False)
    Publication_date = models.DateTimeField
    Journal = models.CharField(max_length = 200, default = '', null = False)
    Volume = models.IntegerField(null = False)
    Issue = models.IntegerField(null = False)
    Article_Description = models.TextField(max_length = 800, default = '', null = False)
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Status = models.CharField(max_length = 6, choices = ArticleStatus.choices, default = ArticleStatus.SAVED)
    def _str_(self):
        return self.Article_Description

class Search(models.Model):
    Search_ID = models.AutoField(primary_key = True)
    Keywords = models.CharField(max_length = 100, default = '')
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Article_ID = models.ForeignKey(Article, on_delete=models.CASCADE)
    def _str_(self):
        return "Search ID: {}/nKeywords: {}/n".format(self.Search_ID, self.Keywords)