# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField


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
    """文章"""
    author = models.ForeignKey(User, on_delete=True)
    Tags = models.ManyToManyField('Tags', verbose_name='标签', blank=True)
    body = MDTextField('正文')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self


class Comment(BaseModel):
    article = models.ForeignKey('Article', on_delete=True)


# 文章类型
class Types(BaseModel):
    typeDesc = models.CharField(max_length=20)


