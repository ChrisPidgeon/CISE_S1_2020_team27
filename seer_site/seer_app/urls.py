from django.urls import path
from seer_app.views import index, submit

urlpatterns = [
    path('', index, name='Home'),
    path('submit/', submit, name='Submit')
]

