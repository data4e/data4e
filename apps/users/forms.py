from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets
from django import forms


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(
            attrs={'placeholder': "password", "class": "form-control"})


class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })


