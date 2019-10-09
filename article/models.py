# Create your models here.
from django.db import models
from mdeditor.fields import MDTextField
from account.models import D4eUser


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('最后更新时间', auto_now=True)
    id = models.AutoField(primary_key=True)
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


# 文章
class Articles(BaseModel):
    """文章"""
    author = models.ForeignKey(D4eUser, on_delete=True)
    tags = models.ManyToManyField('Tags', verbose_name='标签', blank=True)
    body = MDTextField('正文')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print('保存成功!')

    class Meta:
        db_table = 'a_articles'


class Comment(BaseModel):
    article = models.ForeignKey('Articles', on_delete=True)
    parent_comment = models.ForeignKey('self', verbose_name='上级评论', blank=True, null=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(D4eUser, verbose_name='评论人', blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'a_comment'


# 文章类型
class Types(BaseModel):
    type_desc = models.CharField(max_length=20)

    class Meta:
        db_table = 'a_types'


