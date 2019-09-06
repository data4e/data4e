# -*- coding: utf-8 -*-

from MysqlModle.models import Test
from django.shortcuts import render


# 数据库操作
def testMysql(request):
    test1 = Test(name='runoob')
    test1.save()
    context = {'hello': '保存Test成功！'}
    return render(request, 'app.html', context)
