from django.shortcuts import render

# Create your views here.


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        pass
