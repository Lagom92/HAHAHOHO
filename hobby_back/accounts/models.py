from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

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
        blank=True,
        null=True
    )
    userFame = [0,0,0,0]
    followings = models.ManyToManyField('self', related_name="followers", blank=True)

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
