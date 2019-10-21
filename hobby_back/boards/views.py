from .models import PostHobby, PostFree, Faq, Notice, HobbyImage, CommentFree
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer, FaqSerializer, CommentFreeSerializer
from .serializers import ImgSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


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

class commentFree_list(generics.ListCreateAPIView):
    queryset = CommentFree.objects.all()
    serializer_class = CommentFreeSerializer

# class commentFree_detail(generics.RetrieveUpdateDestroyAPIView, pk, comment_pk):
#     queryset = CommentFree.objects.all()
#     serializer_class = CommentFreeSerializer   


@api_view(['GET','PUT','DELETE'])
def commentFree_detail(request, pk, comment_pk):
    try:
        commentfree = CommentFree.objects.get(pk=comment_pk)
    except CommentFree.DoesNotExist:
        raise Http404

    #특정 댓글 조회하기
    if request.method == 'GET':
        serializer = CommentFreeSerializer(commentfree)
        return Response(serializer.data)

    #특정 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentFreeSerializer(commentfree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #특정 댓글 삭제
    elif request.method == 'DELETE':
        commentfree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




