import os
from django.db import models
from django.conf import settings
from accounts.models import User

# 게시판 대분류
class Post(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

# 카테고리 대분류
class Section(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 카테고리 소분류
class Group(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# 취미 게시판
class PostHobby(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    contents = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    startDate = models.DateTimeField()
    regardless = 'NO'
    male = 'MA'
    female = 'FE'
    about_gender = (
        (regardless, 'Regardless'),
        (male, 'Male'),
        (female, 'Female')
    )
    gender = models.CharField(max_length=10, choices=about_gender, default=regardless) 
    age = models.IntegerField()    
    member = models.IntegerField() 
    location = models.CharField(max_length=500) 
    fee = models.IntegerField(default=10000) 

    def __str__(self):
        return self.title

class HobbyImage(models.Model):
    posthobby = models.ForeignKey(PostHobby, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to="hobby/%Y/%m/%d")   
    # delete 오버라이딩
    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.photo.path))
        super(HobbyImage, self).delete(*args, **kwargs)

    def __str__(self):
        return '{}의 img'.format(self.posthobby)

# 자유게시판
class PostFree(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 공지사항 게시판
class Notice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50, default='관리자')
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# FAQ 게시판
class Faq(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 취미게시판 댓글
class CommentHobby(models.Model):
    # 댓글과 1:n
    postHobby = models.ForeignKey(PostHobby, on_delete=models.CASCADE)
    # 유저와 1:n
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.CharField(max_length=100)
    # 생성날짜
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents

# 자유게시판 댓글
class CommentFree(models.Model):
    # 댓글과 1:n
    postFree = models.ForeignKey(PostFree, on_delete=models.CASCADE)
    # 유저와 1:n
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.CharField(max_length=100)
    # 생성날짜
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contents