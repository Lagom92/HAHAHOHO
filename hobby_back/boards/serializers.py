from rest_framework import serializers
from .models import PostFree


class PostFreeserializer(serializers.ModelSerializer):
    class Meta:
        model = PostFree
        fields = '__all__'
