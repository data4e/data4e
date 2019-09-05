from django.shortcuts import render


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, 'app.html', context)


def index(request):
    context = {'title': 'data for everything', 'hello': 'this is index !'}
    return render(request, 'app.html', context)
