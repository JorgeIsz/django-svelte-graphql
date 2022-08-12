from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Task

class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'name')
    fieldsets = ('User', {'fields': ('username', 'name')}),

admin.site.register(User, CustomUserAdmin)
admin.site.register([Task])
