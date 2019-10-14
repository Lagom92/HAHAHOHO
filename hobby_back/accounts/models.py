from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=100)
    userSex = models.CharField(max_length=20)
    userAge = models.IntegerField()
    userImage = models.ImageField(blank=True)
    userGrade = models.IntegerField()

    def __str__(self):
        return self.userName

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

