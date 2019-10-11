# Create your models here.
from django.db import models
from mdeditor.fields import MDTextField
from common.models import BaseModel


# 标签
class Tags(BaseModel):
    name = models.CharField('标签', max_length=20)

    class Meta:
        db_table = 'a_tags'
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        pass


# 文章
class Articles(BaseModel):
    """文章"""
    tags = models.ManyToManyField('Tags', verbose_name='标签', blank=True)
    body = MDTextField('正文')
    title = models.CharField(max_length=64, verbose_name='标题')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print('保存成功!')

    class Meta:
        db_table = 'a_articles'
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Comment(BaseModel):
    article = models.ForeignKey('Articles', on_delete=True)
    parent_comment = models.ForeignKey('self', verbose_name='上级评论', blank=True, null=True, on_delete=models.CASCADE)
    body = models.TextField('body')

    class Meta:
        db_table = 'a_comment'
        verbose_name = '评论'
        verbose_name_plural = '评论'


# 文章类型
class Types(BaseModel):
    type_desc = models.CharField(max_length=20)

    class Meta:
        db_table = 'a_types'
        verbose_name = '文章类型'
        verbose_name_plural = '文章类型'




