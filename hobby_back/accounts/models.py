from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=100)
    userNickName = models.CharField(max_length=100)
    userId = models.CharField(max_length=50)
    userSex = models.CharField(max_length=20)
    userAge = models.CharField(max_length=50)
    userImage = models.ImageField(blank=True)
    userGrade = models.IntegerField(default=1)
    userAddress = models.CharField(max_length=200, blank=True)
    userPoint = models.IntegerField(default=0)
    userLike = ArrayField(
        ArrayField(
            models.CharField(max_length=50, blank=True, default=''),
            size=8,
            blank=True,
            default=list,
            null=True
        ),
        size=2,
        null=True
    )

    def __str__(self):
        return self.userName

class payInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payNum = models.CharField(max_length=100)
    payAmount = models.IntegerField()
    payDate = models.CharField(max_length=100)

class PostOnetone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    answer = models.TextField(blank=True)

# class Image(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     file = ProcessedImageField(
#             upload_to='accounts/images', # 저장위치
#             processors=[ResizeToFill(600,600)], # 크기 지정
#             format='JPEG', # 확장자 변경
#             options={'quality':90}, # 원본의 90퍼센트 품질로 저장
#     	)

class Follow(models.Model):
      following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_follows")
      follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="who_is_followed")
      follow_time = models.DateTimeField(auto_now=True)

      def __unicode__(self):
          return str(self.follow_time)