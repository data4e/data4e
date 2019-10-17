from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={
        'required': '用户名不能为空'
    })
    password = forms.CharField(required=True, error_messages={
        'required': '密码不能为空'
    })


class UserRegisterForm(forms.Form):
    nickname = forms.CharField(required=True, error_messages={
        'required': '昵称不能为空',
    })
    username = forms.CharField(required=True, error_messages={
        'required': '账号不能为空',
    })
    password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })
    verify_new_password = forms.CharField(required=True, min_length=9, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(required=True, error_messages={
        'required': '旧密码不能为空'
    })
    new_password = forms.CharField(required=True, min_length=8, max_length=20, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })
    verify_new_password = forms.CharField(required=True, max_length=20, min_length=8, error_messages={
        'required': '密码不能为空',
        'min_length': '密码长度最少8位',
        'max_length': '密码不能超过20位'
    })



