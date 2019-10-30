from django.contrib import admin
from .models import User, PostOnetone, Follow

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'userName', 'userNickName', 'userSex', 'userAge', 'userGrade', 'userLike', 'userAddress', 'userFame']
    list_display_links = ['userName']

@admin.register(PostOnetone)
class PostOnetoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contents', 'answer']
    list_display_links = ['user']

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ['following']
    list_display_links = []

