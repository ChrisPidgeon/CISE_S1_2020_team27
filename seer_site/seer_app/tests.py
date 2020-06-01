from django.test import TestCase
import datetime
from _datetime import date

from .models import Article
from .models import User
from .models import Account
from .models import Roles
from .models import AccountRoles
from .models import Search

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(User_ID = 1, F_name = "Joe", L_name = "Bloggs", 
        Birth_date = datetime.datetime(2001, 3, 15), Email = "joe.bloggs@test.com")

        Account.objects.create(Account_ID = 1, User_ID = test_user, 
        Username = "JoeBloggs", Password = "asdasdasd")
    
    def test_account_and_user_are_connected_correctly(self):
        test_user = User.objects.get(F_name = "Joe")
        test_account = Account.objects.get(Username = "JoeBloggs")
        self.assertEqual(test_user.User_ID, test_account.User_ID.User_ID)

class ArticleTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(User_ID = 1, F_name = "Joe", L_name = "Bloggs", 
        Birth_date = datetime.datetime(2001, 3, 15), Email = "joe.bloggs@test.com")
        
        Article.objects.create(Title = "test title", Author = "test author", 
        Journal = "test journal", Volume = 2, Issue = 10, 
        Article_Description = "test description", User_ID = test_user, Status = "SUB")
    
    def test_article_and_user_are_connected_correctly(self):
        test_user = User.objects.get(F_name = "Joe", L_name = "Bloggs")
        test_article = Article.objects.get(Title = "test title")
        self.assertEqual(test_user.User_ID, test_article.User_ID.User_ID)

class AccountRolesTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(User_ID = 1, F_name = "Joe", L_name = "Bloggs", 
        Birth_date = datetime.datetime(2001, 3, 15), Email = "joe.bloggs@test.com")

        test_account = Account.objects.create(Account_ID = 1, User_ID = test_user, 
        Username = "JoeBloggs", Password = "asdasdasd")

        test_role = Roles.objects.create(Role_Type = "General User")
        AccountRoles.objects.create(Account_ID = test_account, Role_Type = test_role)

    def test_account_roles_are_defined_correctly(self):
        test_user = User.objects.get(F_name = "Joe", L_name = "Bloggs")
        test_account = Account.objects.get(Username = "JoeBloggs")
        test_role = Roles.objects.get(Role_Type = "General User")
        test_account_roles = AccountRoles.objects.get(Account_ID = test_account, Role_ID = test_role)

        self.assertTrue(test_account_roles.Account_ID.User_ID.User_ID == test_user.User_ID)
        self.assertTrue(test_account_roles.Role_ID.Role_ID == test_role.Role_ID)

class SearchTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(User_ID = 1, F_name = "Joe", L_name = "Bloggs", 
        Birth_date = datetime.datetime(2001, 3, 15), Email = "joe.bloggs@test.com")
        test_article = Article.objects.create(Title = "test title", Author = "test author", 
        Journal = "test journal", Volume = 2, Issue = 10, 
        Article_Description = "test description", User_ID = test_user, Status = "SUB")
        Search.objects.create(Keywords = "Test search keywords", User_ID = test_user, Article_ID = test_article)

    def test_search_is_connected_correctly(self):
        test_user = User.objects.get(F_name = "Joe", L_name = "Bloggs")
        test_article = Article.objects.get(Title = "test title")
        test_search = Search.objects.get(Keywords = "Test search keywords")

        self.assertTrue(test_user.User_ID == test_search.User_ID.User_ID)
        self.assertTrue(test_article.Article_ID == test_search.Article_ID.Article_ID)

