from .models import PostHobby, PostFree, Faq, Notice, HobbyImage
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer, FaqSerializer
from .serializers import ImgSerializer
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

# hobby게시판의 img list
class img_list(generics.ListCreateAPIView):
    queryset = HobbyImage.objects.all()
    serializer_class = ImgSerializer

# hobby게시판의 img detail
class img_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HobbyImage.objects.all()
    serializer_class = ImgSerializer

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
