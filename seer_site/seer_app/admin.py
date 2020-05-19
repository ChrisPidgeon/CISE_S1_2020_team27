from django.contrib import admin

from .models import User
from .models import Account
from .models import Roles
from .models import AccountRoles
from .models import Article
from .models import Search

admin.site.register(User)
admin.site.register(Account)
admin.site.register(Roles)
admin.site.register(AccountRoles)
admin.site.register(Article)
admin.site.register(Search)
