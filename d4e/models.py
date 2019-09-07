# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    id = models.IntegerField(primary_key=True)  # id
    name = models.CharField(max_length=20)
    createTime = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=True)


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=True)


class Nav(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=50)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)


class Links(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    img = models.CharField(max_length=200)
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)


