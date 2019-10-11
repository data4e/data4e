from django.contrib import admin

# Register your models here.
from .models import Articles, Tags, Comment, Types


class ArticleAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'update_time')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('parent_comment', 'create_user', 'create_time')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_desc', 'create_time', 'update_time')


admin.site.register(Articles, ArticleAdmin)
admin.site.register(Tags, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Types, TypeAdmin)
