from django.db import models

# Create your models here.

class Post(models.Model):
    # 어느 게시판인지 체크용 number
    boardName = models.CharField(max_length=50)
    boardNumber = models.IntegerField()
    
    def __str__(self):
        return self.boardName


class PostFree(models.Model):
    # 자유게시판
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    contents = models.TextField()
    createDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


