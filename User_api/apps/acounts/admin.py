from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):

    list_display = ['email', 'name', 'phone', 'date_birth', 'is_staff', 'is_superuser']

    
admin.site.register(User)
