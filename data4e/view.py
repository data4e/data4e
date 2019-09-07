from django.shortcuts import render


Base = 'base.html'
Tools = 'tools.html'


def public_parameter(request):
    nav_list = [
        {'name': '工具', 'link': 'tools'}, {'name': '工具', 'link': 'tools'}, {'name': '工具', 'link': 'tools'}
    ]
    context = {'title': 'data for everything', 'hello': 'this is index !', 'nav_list': nav_list}
    return render(request, Base, context)


def hello(request):
    context = {'hello': 'Hello World!'}
    return render(request, Base, context)


def index(request):
    nav_list = [
        {'name': '工具', 'link': 'tools'}, {'name': '工具', 'link': 'tools'}, {'name': '工具', 'link': 'tools'}
    ]
    context = {'title': 'data for everything', 'hello': 'this is index !', 'nav_list': nav_list}
    return render(request, Base, context)


def login(request):
    context = {'title': '登陆'}
    return render(request, Base, context)


def tools(request):
    context = {'title': 'tools'}
    return render(request, Tools, context)

