from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, PostHobby, PostFree, Notice, Faq
from .models import CommentHobby, CommentFree, ParticipantCheck, Bill

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(PostHobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'subclass', 'title', 'user', 'created_at', 'photo']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'user']
    list_filter = ['subclass', 'gender']

@admin.register(PostFree)
class FreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'title', 'user', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'title', 'contents', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'title', 'contents', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title']

@admin.register(CommentHobby)
class CommentHobbyAdmin(admin.ModelAdmin):
    list_display = ['id', 'postHobby', 'user', 'contents', 'created_at']
    list_display_links = ['id', 'contents']
    search_fields = ['postHobby']

@admin.register(CommentFree)
class CommentFreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'postFree', 'user', 'contents', 'created_at']
    list_display_links = ['id', 'contents']
    search_fields = ['postFree']

@admin.register(ParticipantCheck)
class ParticipantCheckAdmin(admin.ModelAdmin):
    list_display = ['user','post']
    
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'money', 'change', 'created_at']
    list_display_links = ['id', 'user']