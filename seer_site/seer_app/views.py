from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.db.models import Q
from django.views.generic import ListView

def index(request):
    #Luis 20/05/2020 added Articles model table to view
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'seer_app/Home.html', context)


# def searcharticles(request):
#     if request.method == 'GET':
#         query = request.GET.get('q')

#         submitbutton = request.GET.get('submit')

#         if query is not None:
#             lookups = Q(Title__icontains = query)

#             results = Article.objects.filter(lookups).distinct()

#             context = {'results': results, 'submitbutton': submitbutton}

#             return render(request, 'seer_app/Home.html',context)

#         else:
#             return render(request,'seer_app/Home.html')

#     else:
#         return render (request,'seer_app/Home.html')

class SearchResultsView(ListView):
    model = Article
    template_name = 'searchresults.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Article.objects.filter(Q(title__icontains = query))

        return object_list