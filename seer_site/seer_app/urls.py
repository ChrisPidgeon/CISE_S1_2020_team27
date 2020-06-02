from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import SearchResultsView


urlpatterns = [
    path('', views.index, name='Home Page'),
    #url(r'^$',searcharticles, name='searcharticles'),
    path('',SearchResultsView.as_view(), name = 'search_results'),
]


