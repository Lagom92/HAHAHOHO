from django.shortcuts import redirect, get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PostHobby, PostFree, Faq, Notice, HobbyImage, CommentFree
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer
from .serializers import ImgSerializer, FaqSerializer, CommentFreeSerializer

class postHobby_list(generics.ListCreateAPIView):
    '''
    취미 게시판 list page를 생성, 조회 하는 API

    ---
    ## `/boards/hobby/`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - startDate: 모임 시작시간
        - gender: 모임 성별 여부
        - age: 연령대
        - member: 총 인원
        - location: 모임을 할 장소
        - fee: 비용
    '''
    search_fields = ['title', 'contents', 'location']
    filter_backends = (filters.SearchFilter,)
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer
    
class postHobby_detail(generics.RetrieveUpdateDestroyAPIView):
    '''
    취미 게시판 detail page를 조회, 수정, 삭제 하는 API

    ---
    ## `/boards/hobby/{id}/`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - startDate: 모임 시작시간
        - gender: 모임 성별 여부
        - age: 연령대
        - member: 총 인원
        - location: 모임을 할 장소
        - fee: 비용
    '''
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer

# hobby게시판의 img list
class img_list(generics.ListCreateAPIView):
    '''
    취미 게시판의 이미지들을 생성, 조회 하는 API
    
    ---
    ## 내용
        - photo: 이미지
        
    '''
    queryset = HobbyImage.objects.all()
    serializer_class = ImgSerializer

# hobby게시판의 img detail
class img_detail(generics.RetrieveAPIView):
    '''
    취미 게시판의 이미지를 조회 하는 API
    
    ---
    ## 내용
        - photo: 이미지
        
    '''
    queryset = HobbyImage.objects.all()
    serializer_class = ImgSerializer

class postFree_list(generics.ListCreateAPIView):
    '''
    자유 게시판 list page를 생성, 조회 하는 API
    
    ---
    ## `/boards/free/`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - startDate: 모임 시작 시간
        - created_at: 게시판 작성 시간
        - group: 카테고리 소분류
        - user: 게시판 작성자
    '''
    search_fields = ['title', 'contents']
    filter_backends = (filters.SearchFilter,)
    queryset = PostFree.objects.all()
    serializer_class = PostFreeSerializer

class postFree_detail(generics.RetrieveUpdateDestroyAPIView):
    '''
    자유 게시판 detail page를 조회, 수정, 삭제 하는 API
    
    ---
    ## `/boards/free/{id}/`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - startDate: 모임 시작 시간
        - created_at: 게시판 작성 시간
        - group: 카테고리 소분류
        - user: 게시판 작성자
    '''
    queryset = PostFree.objects.all()
    serializer_class = PostFreeSerializer

class notice_list(generics.ListAPIView):
    '''
    공지사항 게시판 list page를 조회 하는 API
    
    ---
    ## `/boards/notice/`
    ## 내용
        - title: 게시판 제목
        - name: 게시판 작성자
        - contents: 게시판 내용
        - created_at: 게시판 작성 시간
    '''
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class notice_detail(generics.RetrieveAPIView):
    '''
    공지사항 게시판 detail page를 조회 하는 API
    
    ---
    ## `/boards/notice/{id}/`
    ## 내용
        - title: 게시판 제목
        - name: 게시판 작성자
        - contents: 게시판 내용
        - created_at: 게시판 작성 시간
    '''
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class faq_list(generics.ListAPIView):
    '''
    FAQ 게시판 list page를 조회 하는 API
    
    ---
    ## `/boards/faq/`
    ## 내용
        - title: 게시판 제목
        - name: 게시판 작성자
        - contents: 게시판 내용
        - created_at: 게시판 작성 시간
    '''
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class faq_detail(generics.RetrieveAPIView):
    '''
    FAQ 게시판 detail page를 조회 하는 API
    
    ---
    ## `/boards/faq/{id}/`
    ## 내용
        - title: 게시판 제목
        - name: 게시판 작성자
        - contents: 게시판 내용
        - created_at: 게시판 작성 시간
    '''
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class commentFree_list(generics.ListCreateAPIView):
    queryset = CommentFree.objects.all()
    serializer_class = CommentFreeSerializer

# 체크! pk와 question_pk는 어디서 사용되는가???
@api_view(['GET','PUT','DELETE'])
def commentFree_detail(request, pk, comment_pk):
    commentfree = get_object_or_404(CommentFree, pk=question_id)
    # 특정 댓글 조회하기
    if request.method == 'GET':
        serializer = CommentFreeSerializer(commentfree)
        return Response(serializer.data)

    # 특정 댓글 수정
    elif request.method == 'PUT':
        serializer = CommentFreeSerializer(commentfree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # 특정 댓글 삭제
    elif request.method == 'DELETE':
        commentfree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
