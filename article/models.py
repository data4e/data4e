# Create your models here.
from django.db import models
from mdeditor.fields import MDTextField
from django.conf import settings


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('最后更新时间', auto_now=True)
    delete_flag = (
        (1, '删除'),
        (0, '正常')
    )

    class Meta:  # 抽象
        abstract = True


# 标签
class Tags(BaseModel):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'a_tags'
        verbose_name = '标签'


# 文章
class Articles(BaseModel):
    """文章"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True)
    tags = models.ManyToManyField('Tags', verbose_name='标签', blank=True)
    body = MDTextField('正文')
    title = models.CharField(max_length=64, verbose_name='标题')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print('保存成功!')

    class Meta:
        db_table = 'a_articles'
        verbose_name = '文章'


class Comment(BaseModel):
    article = models.ForeignKey('Articles', on_delete=True)
    parent_comment = models.ForeignKey('self', verbose_name='上级评论', blank=True, null=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='评论人', blank=False, null=False,
                                on_delete=models.CASCADE)

    class Meta:
        db_table = 'a_comment'


# 文章类型
class Types(BaseModel):
    type_desc = models.CharField(max_length=20)

    class Meta:
        db_table = 'a_types'
        verbose_name = '文章类型'


