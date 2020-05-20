from django.shortcuts import render
from django.http import HttpResponse
from seer_app.models import Article

def index(request):
    #Luis 20/05/2020 added Articles model table to view
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'seer_app/Home.html', context)
