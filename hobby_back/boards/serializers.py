from rest_framework import serializers
from .models import PostHobby, PostFree, Notice, Faq, HobbyImage, CommentFree

class PostHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHobby
        fields = '__all__'

class PostFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFree
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyImage
        fields = '__all__'
        
class CommentFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFree
        fields = '__all__'

