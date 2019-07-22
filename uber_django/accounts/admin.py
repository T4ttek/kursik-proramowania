from django.contrib import admin

# Register your models here.
from django.contrib import admin

from accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user_type', 'is_mature']
