from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

from .forms import submitArticleForm

def index(request):
    #Luis 20/05/2020 added Articles model table to view
    articles = Article.objects.all()
    context = {
        'articles': articles
        }
    return render(request, 'seer_app/Home.html', context)

def submit(request):
    form = submitArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = submitArticleForm()
    
    context = {
        'form' : form
    }

    return render(request, 'seer_app/SubmitForm.html', context)