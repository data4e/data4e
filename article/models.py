# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    id = models.IntegerField(primary_key=True)
    deleteFlag = (
        (1, '删除'),
        (0, '正常')
    )


# 标签
class Tags(BaseModel):
    name = models.CharField(max_length=20)


# 文章
class Article(BaseModel):
    author = models.ForeignKey(User, on_delete=True)


class Comment(BaseModel):
    article = models.ForeignKey('Article', on_delete=True)


# 导航
class Nav(BaseModel):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=50)


# 链接
class Links(BaseModel):
    title = models.CharField(max_length=20)
    url = models.CharField(max_length=50)
    img = models.CharField(max_length=200)


# 文章类型
class Types(BaseModel):
    typeDesc = models.CharField(max_length=20)


