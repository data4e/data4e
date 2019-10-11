from django.db import models
from django.conf import settings
# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('最后更新时间', auto_now=True)
    delete_flag = models.IntegerField(default=0, editable=False)
    create_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=True, verbose_name='创建人')

    class Meta:  # 抽象
        abstract = True


class Link(BaseModel):
    """友情连接"""
    link = models.CharField(max_length=64, verbose_name='连接')
    desc = models.CharField(max_length=32, verbose_name='描述')

    class Meta:
        db_table = 'sys_link'
        verbose_name = '友情连接'
        verbose_name_plural = '友情连接'

    def __str__(self):
        return self.link


class Dict(BaseModel):
    dict_code = models.CharField(max_length=20, verbose_name='字典码')
    dict_desc = models.CharField(max_length=32, verbose_name='字典项')
    dict_type = models.ForeignKey('DictType', on_delete=True, verbose_name='字典类型')

    class Meta:
        db_table = 'sys_dict'
        verbose_name = '数据字典'
        verbose_name_plural = '数据字典'

    def __str__(self):
        return self.dict_desc


class DictType(BaseModel):
    type_code = models.CharField(max_length=20, verbose_name='字典类型码')
    type_desc = models.CharField(max_length=32, verbose_name='字典类型描述')

    class Meta:
        db_table = 'sys_dict_type'
        verbose_name = '数据字典类型'
        verbose_name_plural = '数据字典类型'

    def __str__(self):
        return self.type_desc
