# Generated by Django 2.2.6 on 2019-10-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20191011_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dict',
            name='delete_flag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dicttype',
            name='delete_flag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='link',
            name='delete_flag',
            field=models.IntegerField(default=0),
        ),
    ]
