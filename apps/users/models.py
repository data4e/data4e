from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from common.models import BaseModel


class D4eUser(AbstractUser):
    """用户"""
    nickname = models.CharField('昵称', max_length=120, blank=True)
    birth = models.DateField('生日', null=True)
    avatar = models.CharField(max_length=256)
    qq = models.CharField(max_length=16)
    web_site = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        return AbstractUser.save(self)

    class Meta(AbstractUser.Meta):
        db_table = 'u_user'
        verbose_name = '用户'


class UserFavorite(models.Model):
    """用户收藏"""
    user_id = models.IntegerField()
    favorite_id = models.IntegerField()
    favorite_type = models.IntegerField()

    class Meta:
        db_table = 'u_user_favorite'
        verbose_name = '用户收藏'


class Notification(BaseModel):
    """消息、通知"""
    title = models.CharField(max_length=128)
    body = models.TextField()
    status = models.IntegerField()

    class Meta:
        db_table = 'notification'
        verbose_name = '消息'
