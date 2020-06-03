from django.shortcuts import render
from django.http import HttpResponse
from seer_app.models import Article
from django.db.models import Q

from .forms import submitArticleForm, uploadBibtexForm

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

def search(request):
    if request.method == 'GET':
        query=request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query:
            lookups = (
                Q(Title__icontains = query) |
                Q(Author__icontains = query)
                )
            #searchByAuthor = Q(Author__icontains = query)
            results = Article.objects.filter(lookups).distinct()

            context={'results': results,'submitbutton': submitbutton}

            return render(request,'seer_app/search_results.html',context)

        else:
            return render(request, 'seer_app/search_results.html')
    else:

        return render(request,'seer_app/search_results.html')

def upload(request):
    form = uploadBibtexForm(request.POST or None)

    context = {
        'form' : form
    }
    return render(request, 'seer_app/upload.html', context)