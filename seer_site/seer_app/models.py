import datetime

from django.db import models
from django.utils import timezone
from enum import Enum
from django.utils.translation import gettext_lazy as _
from _datetime import date
import django

# Create your models here.

class User(models.Model):
    class Meta():
        verbose_name_plural = "Users"
    
    User_ID = models.AutoField(primary_key = True, verbose_name=("User ID"))
    F_name = models.CharField(max_length = 40, default = '', null = False, verbose_name=("First Name"))
    L_name = models.CharField(max_length = 40, default = '', null = False, verbose_name=("Last Name"))
    Birth_date = models.DateField('Birth Date', default = django.utils.timezone.now)
    Email = models.CharField(max_length = 80, default = '', null = False)
    Created = models.DateTimeField(auto_now_add = True, verbose_name = "Creation Date")
    def __str__(self):
        return self.F_name + ' ' + self.L_name 
    objects = models.Manager()


class Account(models.Model):
    class Meta():
        verbose_name_plural = "Accounts"

    Account_ID = models.AutoField(primary_key = True, verbose_name=("Account ID"))
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User ID"))
    Username = models.CharField(max_length = 40, default = '', null = False, verbose_name=("User Name"))
    Password = models.CharField(max_length = 40, default = '', null = False)
    Created = models.DateTimeField(auto_now_add = True, verbose_name = "Creation Date")
    def _str_(self):
        return self.Username
    objects = models.Manager()

class Roles(models.Model):
    class Meta():
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    class RoleType(models.TextChoices):
        SUBMITTER = 'ROLE_S', _('Submitter')
        MODERATER = 'ROLE_M', _('Moderator')
        ANALYST = 'ROLE_A', _('Analyst')
        GENERAL_USER = 'ROLE_G', _('General User')

    Role_ID = models.AutoField(primary_key = True, verbose_name=("Role ID"))
    Role_Type = models.CharField(max_length = 6, choices = RoleType.choices, default = RoleType.GENERAL_USER)
    Created = models.DateTimeField(auto_now_add = True, verbose_name = "Creation Date")
    def _str_(self):
        return self.Role_Type
    objects = models.Manager()    

class AccountRoles(models.Model):
    class Meta():
        verbose_name = "Account Role"
        verbose_name_plural = "Account Roles"

    Account_ID = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name=("Account ID"))
    Role_ID = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name=("Role ID"))
    Created = models.DateTimeField(auto_now_add = True, verbose_name = "Creation Date")
    def _str_(self):
        return "Account ID: {}".format(self.Account_ID)
    objects = models.Manager()

class Article(models.Model):
    class Meta():
        verbose_name_plural = "Articles"

    class ArticleStatus(models.TextChoices):
        SUBMITTED = 'SUB', _('Submitted')
        IN_MODERATION = 'IN_MOD', _('In Moderation')
        MODERATED = 'MOD', _('Moderated')
        IN_ANALYSIS = 'IN_ANA', _('In Analysis')
        ANALYZED = 'ANA', _('Analyzed')

    Article_ID = models.AutoField(primary_key = True, verbose_name=("Article ID"))
    Title = models.CharField(max_length = 100, default = '', null = False)
    Author = models.CharField(max_length = 100, default = '', null = False)
    Publication_date = models.DateField('Publication Date', default = django.utils.timezone.now)
    Journal = models.CharField(max_length = 200, default = '', null = False)
    Volume = models.IntegerField(null = False)
    Issue = models.IntegerField(null = False)
    Article_Description = models.TextField(max_length = 800, default = '', null = False, verbose_name=("Description"))
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User ID"))
    Status = models.CharField(max_length = 6, choices = ArticleStatus.choices, default = ArticleStatus.SUBMITTED)
    Created = models.DateTimeField(auto_now_add = True, verbose_name = "Creation Date")
    def _str_(self):
        return self.Title
    objects = models.Manager()

class Search(models.Model):
    class Meta():
        verbose_name_plural = "Searches"

    Search_ID = models.AutoField(primary_key = True, verbose_name=("Search ID"))
    Keywords = models.CharField(max_length = 100, default = '')
    User_ID = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=("User ID"))
    Article_ID = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name=("Article ID"))    
    Created = models.DateTimeField(auto_now_add = True, verbose_name = "Creation Date")
    def _str_(self):
        return self.Search_ID
    objects = models.Manager()