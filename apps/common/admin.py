from django.contrib import admin
from .models import Link, DictType, Dict
# Register your models here.


class LinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'desc', 'create_time', 'create_user')


class DictAdmin(admin.ModelAdmin):
    list_display = ('dict_code', 'dict_desc', 'dict_type',  'create_time', 'create_user')


class DictTypeAdmin(admin.ModelAdmin):
    list_display = ('type_code', 'type_desc', 'create_time', 'create_user')


admin.site.register(Link, LinkAdmin)
admin.site.register(DictType, DictTypeAdmin)
admin.site.register(Dict, DictAdmin)
