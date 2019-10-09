from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager


class D4eUser(AbstractUser):
    nickname = models.CharField('昵称', max_length=120, blank=True)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)
    age = models.IntegerField('年龄', null=True)
    sex = (
        (1, '男'),
        (2, '女'),
        (3, '保密')
    )

    def save(self, *args, **kwargs):
        return AbstractUser.save(self)

    class Meta(AbstractUser.Meta):
        db_table = 'u_user'
