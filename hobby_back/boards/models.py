from django.db import models
from accounts.models import User

# 게시판
class Post(models.Model):
    boardName = models.CharField(max_length=50)
    boardNumber = models.IntegerField()
    
    def __str__(self):
        return self.boardName


# 카테고리 대분류
class Section(models.Model):
    sectionName = models.CharField(max_length=50)

    def __str__(self):
        return self.sectionName


# 카테고리 소분류
class Group(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    groupName = models.CharField(max_length=50)

    def __str__(self):
        return self.groupName


# 취미 게시판
class PostHobby(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)    # 제목
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자
    contents = models.TextField()   # 내용
    createDate = models.DateTimeField(auto_now_add=True)    # 글 생성 날짜
    startDate = models.DateTimeField()  # 모임 모집에 대한 시작 시간
    endDate = models.DateTimeField()    # 모임 모집에 대한 마감 시간
    totalMember = models.IntegerField()  # 참여 인원
    nowMember = models.IntegerField()   # 현재 인원
    location = models.CharField(max_length=300) # 장소
    fee = models.IntegerField() # 회비

    def __str__(self):
        return self.title


# 자유게시판
class PostFree(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    createDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 공지사항 게시판
class Notice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    contents = models.TextField()
    createDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# F&Q 게시판
class Faq(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    contents = models.TextField()
    createDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# 취미게시판 댓글
class CommentHobby(models.Model):
    # 댓글과 1:n
    postHobby = models.ForeignKey(PostHobby, on_delete=models.CASCADE)
    # 유저와 1:n
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    # 생성날짜
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


# 자유게시판 댓글
class CommentFree(models.Model):
    # 댓글과 1:n
    postFree = models.ForeignKey(PostFree, on_delete=models.CASCADE)
    # 유저와 1:n
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    # 생성날짜
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content