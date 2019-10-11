from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })



