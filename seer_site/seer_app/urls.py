from django.urls import path
from django.conf.urls import url
from .views import (searchposts)

from . import views





urlpatterns = [
    path('', views.index, name='Home Page'),
    path('search/',views.searchposts,name='search_results'),

    url(r'^$',searchposts,name='searchposts'),
    
]


