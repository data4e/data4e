from django.conf.urls import url
from django.contrib.auth import views as auth_view
from django.urls import path
from . import views
from .forms import LoginForm

app_name = 'account'

urlpatterns = [
    url(r'^login/', LoginForm),
]
