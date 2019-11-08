from django.contrib import admin
from .models import User, KakaoBill

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'userName', 'userNickName', 'userSex',
        'userAge', 'userGrade', 'userLike', 'userAddress'
    ]
    list_display_links = ['id', 'userName']

@admin.register(KakaoBill)
class KakaoBillAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'money', 'change', 'created_at']
    list_display_links = ['id', 'user']
