from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostFreeserializer
from .models import PostFree
# Create your views here.


class PostFreeViewSet(viewsets.ModelViewSet):
    queryset = PostFree.objects.all()
    serializer_class = PostFreeserializer



