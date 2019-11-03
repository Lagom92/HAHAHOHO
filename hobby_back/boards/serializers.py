from rest_framework import serializers
from .models import PostHobby, PostFree, Notice, Faq, CommentFree, ParticipantCheck, CommentHobby

class ParticipantCheckSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ParticipantCheck
        fields = '__all__'
        
class PostHobbySerializer(serializers.ModelSerializer):
    # participant = ParticipantCheckSerializer(many=True, read_only=True)
    username = serializers.CharField(source="user.userNickName")
    userimage = serializers.CharField(source="user.userImage")
    postname = serializers.CharField(source="post.name")
    subclassname = serializers.CharField(source="subclass.name")

    class Meta:
        model = PostHobby
        fields = '__all__'

class PostFreeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.userNickName")

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

class CommentFreeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.userNickName")

    class Meta:
        model = CommentFree
        fields = '__all__'

class CommentHobbySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.userNickName")

    class Meta:
        model = CommentHobby
        fields = '__all__'
