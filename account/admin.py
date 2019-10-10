from django.contrib import admin

# Register your models here.

from .models import D4eUser
from django.contrib.auth.admin import UserAdmin


admin.site.register(D4eUser, UserAdmin)
