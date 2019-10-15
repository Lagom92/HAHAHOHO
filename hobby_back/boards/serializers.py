from rest_framework import serializers
from .models import PostHobby, PostFree

class PostHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHobby
        fields = '__all__'


class PostFreeserializer(serializers.ModelSerializer):
    class Meta:
        model = PostFree
        fields = '__all__'

