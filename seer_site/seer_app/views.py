from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.db.models import Q
import datetime

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


def advancedsearch(request):
    if request.method == "POST":
        start_date = request.POST.get('startDate')

        end_date = request.POST.get('endDate')

        search_field = request.POST.get('field')

        search_operator = request.POST.get('operator')

        search_keyword = request.POST.get('advkeyword')

        submitbutton = request.POST.get('submit')

        print (search_field)
        print (search_operator)

        if start_date:
            aq = Article.objects.filter(Publication_date__range=(start_date, end_date)).order_by('-Publication_date')

            if search_operator == 'contain':

                if search_field == 'title':
                    final_result = aq.filter(Title__icontains=search_keyword)

                elif search_field == 'author':
                    final_result = aq.filter(Author__icontains=search_keyword)

                elif search_field == 'description':
                    final_result = aq.filter(Article_Description__icontains=search_keyword)

            elif search_operator == 'notcontain':

                if search_field == 'title':
                    final_result = ~aq.filter(Title__icontains=search_keyword)

                elif search_field == 'author':
                    final_result = ~aq.filter(Author__icontains=search_keyword)

                elif search_field == 'description':
                    final_result = ~aq.filter(Article_Description__icontains=search_keyword)

            elif search_operator == 'beginswith':
                
                if search_field == 'title':
                    final_result = aq.filter(Title__istartswith=search_keyword)

                elif search_field == 'author':
                    final_result = aq.filter(Author__istartswith=search_keyword)

                elif search_field =='description':
                    final_result = aq.filter(Article_Description__istartswith=search_keyword)

            elif search_operator == 'endswith':
                
                if search_field == 'title':
                    final_result = aq.filter(Title__iendswith=search_keyword)

                elif search_field == 'author':
                    final_result = aq.filter(Author__iendswith=search_keyword)

                elif search_field =='description':
                    final_result = aq.filter(Article_Description__iendswith=search_keyword)

            elif search_operator == 'equals':
                
                if search_field == 'title':
                    final_result = aq.filter(Title__iexact=search_keyword)

                elif search_field == 'author':
                    final_result = aq.filter(Author__iexact=search_keyword)

                elif search_field =='description':
                    final_result = aq.filter(Article_Description__iexact=search_keyword)


            context={'final_result' : final_result,'submitbutton' : submitbutton}

            return render(request,'seer_app/advancedsearch.html',context)

        else:
            return render(request,'seer_app/advancedsearch.html')
    else:
        return render(request,'seer_app/advancedsearch.html')

# def upload(request):
#     form = uploadBibtexForm(request.POST or None)

#     context = {
#         'form' : form
#     }
#     return render(request, 'seer_app/upload.html', context)