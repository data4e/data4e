from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager


class D4eUser(AbstractUser):
    """用户"""
    nickname = models.CharField('昵称', max_length=120, blank=True)
    age = models.IntegerField('年龄', null=True)
    avatar = models.CharField(max_length=256)
    qq = models.CharField(max_length=16)
    web_site = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        return AbstractUser.save(self)

    class Meta(AbstractUser.Meta):
        db_table = 'u_user'
        verbose_name = '用户'
