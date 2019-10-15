from django.shortcuts import render


Base = 'base.html'
Tools = 'tools.html'
Article = 'article.html'
AddArticle = 'addOrUpdateArticle.html'
Login = 'login.html'


def public_parameter(request):
    nav_list = [
        {'name': '工具', 'link': 'tools'}, {'name': '工具', 'link': 'tools'}, {'name': '工具', 'link': 'tools'}
    ]
    context = {'title': 'data for everything', 'hello': 'this is index !', 'nav_list': nav_list}
    return render(request, Base, context)


def article(request):
    context = {'hello': 'Hello World!'}
    return render(request, Article, context)


def index(request):
    return render(request, Base)


def tools(request):
    context = {'title': 'tools'}
    return render(request, Tools, context)


def handler_404(request):
    return render(request, '404.html')


def handler_500(request):
    return render(request, '500.html')


