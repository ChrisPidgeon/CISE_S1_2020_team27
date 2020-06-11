from django.urls import path
from seer_app.views import index, submit, search
from django.conf.urls import url
from .views import (search,advancedsearch)


urlpatterns = [
    path('', index, name='Home'),
    path('submit/', submit, name='Submit'),
    path('search/',search,name='search_results'),
    path('advanced/',advancedsearch,name='AdvancedSearch'),

    url(r'^$',search,name='searchposts'),
    url(r'^$',advancedsearch,name='advancedsearch'),
]

