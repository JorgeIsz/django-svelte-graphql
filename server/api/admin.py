from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):

    list_display = ('username', 'name')
    fieldsets = ('User', {'fields': ('username', 'name')}),

admin.site.register(User, CustomUserAdmin)
