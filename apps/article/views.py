from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'article-list.html')


def add(request):
    if request.method == 'GET':
        return render(request, 'article-edit.html')
