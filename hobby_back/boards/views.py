from .models import PostHobby, PostFree, Faq, Notice
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer, FaqSerializer
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class postHobby_list(generics.ListCreateAPIView):
    search_fields = ['title', 'contents', 'location']
    filter_backends = (filters.SearchFilter,)
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer
    

class postHobby_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer

class postFree_list(generics.ListCreateAPIView):
    search_fields = ['title', 'contents']
    filter_backends = (filters.SearchFilter,)
    queryset = PostFree.objects.all()
    serializer_class = PostFreeSerializer

class postFree_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostFree.objects.all()
    serializer_class = PostFreeSerializer

class notice_list(generics.ListCreateAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class notice_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class faq_list(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class faq_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
