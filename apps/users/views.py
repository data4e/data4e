from django.shortcuts import render

# Create your views here.


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        pass


def user_list(request):
    print('请求用户列表')
    return render(request, '{message : 用户列表}')

