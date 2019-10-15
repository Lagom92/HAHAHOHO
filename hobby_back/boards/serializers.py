from rest_framework import serializers
from .models import PostHobby

class PostHobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostHobby
        fields = '__all__'