from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class UserRegisterForm(forms.Form):
    nickname = forms.CharField(required=True)
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })
    repeat_password = forms.CharField(required=True, min_length=9, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })



