# Generated by Django 2.2.6 on 2019-10-11 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='d4euser',
            name='age',
        ),
        migrations.AddField(
            model_name='d4euser',
            name='birth',
            field=models.DateField(null=True, verbose_name='生日'),
        ),
    ]