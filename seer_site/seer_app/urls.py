from django.urls import path
from seer_app.views import index, submit

urlpatterns = [
    path('', index, name='Home Page'),
    path('submit/', submit, name='Submit')
]

