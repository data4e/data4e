from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name=''),
    path('edit/', views.add, name='edit')
]
