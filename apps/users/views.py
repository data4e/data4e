from django.shortcuts import render, redirect, reverse
from .forms import UserRegisterForm, UserLoginForm
from .models import D4eUser
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def user_login(request):
    """用户登陆"""
    if request.method == 'GET':
        return render(request, 'sign-in.html')
    else:
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('index'))
            else:
                return render(request, 'sign-in.html', {
                    'msg': '用户名或者密码错误'
                })
        else:
            return render(request, 'sign-in.html', {
                'user_login_form': user_login_form
            })


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

                login(request, a)
                return redirect(reverse('index'))
        else:
            return render(request, 'register.html', {
                'user_register_form': user_register_form
            })


def user_logout(request):
    logout(request)
    return render(request, 'sign-in.html')


def profile(request):
    return render(request, 'profile.html')


