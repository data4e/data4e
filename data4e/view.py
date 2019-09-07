from django.shortcuts import render


Base = 'base.html'
Tools = 'tools.html'


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, Base, context)


def index(request):
    context = {'title': 'data for everything', 'hello': 'this is index !'}
    return render(request, Base, context)


def login(request):
    context = {'title': '登陆'}
    return render(request, Base, context)


def tools(request):
    context = {'title': 'tools'}
    return render(request, Tools, context)

