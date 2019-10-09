from django.contrib import admin

# Register your models here.
from .models import Articles, Tags, Comment, Types

admin.site.register(Articles)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(Types)
