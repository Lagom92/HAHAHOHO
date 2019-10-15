from rest_framework import serializers
from .models import PostHobby, PostFree, Notice, Faq

class PostHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHobby
        fields = '__all__'


class PostFreeserializer(serializers.ModelSerializer):
    class Meta:
        model = PostFree
        fields = '__all__'

class Noticeserializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

class Faqserializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'

