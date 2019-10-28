from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category, Subclass
from .models import PostHobby, PostFree, Notice, Faq, HobbyImage
from .models import CommentHobby, CommentFree

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(Subclass)
class SubclassAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name']
    list_display_links = ['id', 'name']

class ImgInline(admin.StackedInline):
    model = HobbyImage
    readonly_fields = ['photo_image']

    def photo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
            )
        )

@admin.register(PostHobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'subclass', 'title', 'user', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'user']
    list_filter = ['subclass', 'gender']

    inlines = [ImgInline]

@admin.register(PostFree)
class FreeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'subclass', 'title', 'user', 'created_at']
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

@admin.register(HobbyImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'posthobby']
    list_display_links = ['id', 'posthobby']
    readonly_fields = ['photo_image']
    search_fields = ['posthobby']

    def photo_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
            )
        )

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
