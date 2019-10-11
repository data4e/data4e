from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm
from .models import D4eUser
# Create your views here.


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        pass


def user_list(request):
    print('请求用户列表')
    return render(request, '{message : 用户列表}')


def user_register(request):
    """用户注册"""
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            username = user_register_form.cleaned_data['username']
            password = user_register_form.cleaned_data['password']
            user_lists = D4eUser.objects.filter(username=username)
            if user_lists:
                return render(request, 'register.html', {
                    'msg': '用户已经存在！'
                })
            else:
                a = D4eUser()
                a.username = username
                a.set_password(password)
                a.save()
                return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


