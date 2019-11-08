from django.conf import settings
from django.db import models

class User(models.Model):
    userName = models.CharField(max_length=100)
    userNickName = models.CharField(max_length=100)
    userId = models.CharField(max_length=50)
    userSex = models.CharField(max_length=20)
    userAge = models.CharField(max_length=50)
    userImage = models.ImageField(blank=True)
    userGrade = models.IntegerField(default=1)
    userAddress = models.CharField(max_length=200, blank=True)
    userPoint = models.IntegerField(default=5000)
    userLike = models.CharField(max_length=1000, blank=True)
    followings = models.ManyToManyField('self', related_name="followers", symmetrical=False, blank=True)

    def __str__(self):
        return self.userName
  
class payInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payNum = models.CharField(max_length=100)
    payAmount = models.IntegerField()
    payDate = models.CharField(max_length=100)

class KakaoBill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    money = models.IntegerField()
    change = models.CharField(max_length=50)

    def __str__(self):
        return self.change
