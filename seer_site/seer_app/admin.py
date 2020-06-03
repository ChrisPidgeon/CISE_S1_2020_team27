from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import User
from .models import Account
from .models import Roles
from .models import AccountRoles
from .models import Article
from .models import Search

admin.site.site_header = "SEER Administration"

class UserAdmin(admin.ModelAdmin):
    list_display = ('User_ID', 'F_name', 'L_name', 'Email')
    list_filter = ('Created',)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('Account_ID', 'User_ID', 'Username')
    list_filter = ('Created',)

class RolesAdmin(admin.ModelAdmin):
    list_display = ('Role_ID', 'Role_Type')
    list_filter = ('Created',)

class AccountRolesAdmin(admin.ModelAdmin):
    list_display = ('Account_ID', 'Role_ID')
    list_filter = ('Created',)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Article_ID', 'Title', 'Status')
    list_filter = ('Created',)
   
    def make_submitted(self, request, queryset):
        queryset.update(Status = "SUB")
    make_submitted.short_description = "Mark selected articles as submitted"

    def make_in_moderation(self, request, queryset):
        queryset.update(Status = "IN_MOD")
    make_in_moderation.short_description = "Mark selected articles as in moderation"

    def make_moderated(self, request, queryset):
        queryset.update(Status = "MOD")
    make_moderated.short_description = "Mark selected articles as moderated"

    def make_in_analysis(self, request, queryset):
        queryset.update(Status = "IN_ANA")
    make_in_analysis.short_description = "Mark selected articles as in analysis"
    
    def make_analyzed(self, request, queryset):
        queryset.update(Status = "ANA")
    make_analyzed.short_description = "Mark selected articles as analyzed"

    actions = [make_submitted, make_in_moderation, make_moderated, make_in_analysis, make_analyzed]

class SearchAdmin(admin.ModelAdmin):
    list_display = ('Search_ID', 'Keywords')
    list_filter = ('Created',)

admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(AccountRoles, AccountRolesAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Search, SearchAdmin)
