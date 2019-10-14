from django.contrib import admin
from .models import Post, PostFree
# from .models import Post, PostHobby, PostFree, Notice, Faq

admin.site.register(Post)
# admin.site.register(PostHobby)
admin.site.register(PostFree)
# admin.site.register(Notice)
# admin.site.register(Faq)
