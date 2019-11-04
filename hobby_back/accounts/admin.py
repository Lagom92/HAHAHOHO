from django.contrib import admin
from .models import User, PostOnetone, KakaoBill

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'userName', 'userNickName', 'userSex', 'userAge', 
        'userGrade', 'userLike', 'userAddress', 'userFame'
    ]
    list_display_links = ['id', 'userName']

@admin.register(PostOnetone)
class PostOnetoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contents', 'answer']
    list_display_links = ['id', 'user']

@admin.register(KakaoBill)
class KakaoBillAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'money', 'change', 'created_at']
    list_display_links = ['id', 'user']
