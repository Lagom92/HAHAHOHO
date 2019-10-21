from django.contrib import admin
from .models import Post, Section, Group
from .models import PostHobby, HobbyImage, PostFree, Notice, Faq
from .models import CommentHobby, CommentFree

admin.site.register(Post)
admin.site.register(PostHobby)
admin.site.register(HobbyImage)
admin.site.register(PostFree)
admin.site.register(Notice)
admin.site.register(Faq)
admin.site.register(Section)
admin.site.register(Group)
admin.site.register(CommentHobby)
admin.site.register(CommentFree)
