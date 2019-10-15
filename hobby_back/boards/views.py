from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PostHobby, PostFree, Faq, Notice
from .serializers import PostHobbySerializer, PostFreeserializer, Noticeserializer, Faqserializer

#취미게시판 
@api_view(['GET', 'POST'])
def postHobby_list(request):
    # Read
    if request.method == 'GET':
        queryset = PostHobby.objects.all()
        serializer = PostHobbySerializer(queryset, many=True)
        return Response(serializer.data)

    # Create
    elif request.method == 'POST':
        serializer = PostHobbySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def postHobby_detail(request, id):
    try:
        postHobby = PostHobby.objects.get(id=id)
    except postHobby.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Detail
    if request.method == 'GET':
        serializer = PostHobbySerializer(postHobby)
        return Response(serializer.data)

    # Update
    elif request.method == 'PUT':
        serializer = PostHobbySerializer(postHobby, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete
    elif request.method == 'DELETE':
        postHobby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#자유게시판
@api_view(['GET','POST'])
def postFree_list(request):
    #자유게시판 조회기능
    if request.method == 'GET':
        queryset = PostFree.objects.all()
        serializer = PostFreeserializer(queryset, many = True)
        return Response(serializer.data)


    #자유게시판 글 생성기능
    elif request.method == 'POST':
        serializer = PostFreeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def postFree_detail(request,id):
    try:
        postfree = PostFree.objects.get(id=id)
    except PostFree.DoesNotExist:

        return Response(status= status.HTTP_404_NOT_FOUND)

    #특정 게시글 조회하기
    if request.method == 'GET':
        serializer = PostFreeserializer(postfree)
        return Response(serializer.data)

    #특정 게시글 수정
    elif request.method == 'PUT':
        serializer = PostFreeserializer(postfree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        postfree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# 공지사항 게시판
@api_view(['GET','POST'])
def notice_list(request):
    #공지사항 조회기능
    if request.method == 'GET':
        queryset = Notice.objects.all()
        serializer = Noticeserializer(queryset, many = True)
        return Response(serializer.data)

    #공지사항 글 생성 기능
    elif request.method == 'POST':
        serializer = Noticeserializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','DELETE'])
def notice_detail(request, id):
    try:
        notice = Notice.objects.get(id=id)
    except Notice.DoesNotExist:
        return Response(status.HTTP__404_NOT_FOUND)

    #특정 공지사항글 조회하기

    if request.method == 'POST':
        serializer = Noticeserializer(notice)
        return Response(serializer.data)

    #특정 공지사항 글 수정하기

    elif request.method == 'PUT':
        serializer = Noticeserializer(notice, data= request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    #특정 공지사항글 삭제
    elif request.method == 'DELETE':
        notice.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# FAQ
@api_view(['GET', 'POST'])
def faq_list(request):
    # FAQ게시판 조회기능
    if request.method == 'GET':
        queryset = Faq.objects.all()
        serializer = Faqserializer(queryset, many=True)
        return Response(serializer.data)

    # FAQ게시판 글쓰기 기능

    elif request.method =='POST':
        serializer = Faqserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def faq_detail(request, id):
    try:
        faq = Faq.objects.get(id=id)
    except Faq.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    #특정FAQ게시글 조회
    if request.method == 'GET':
        serializer = Faqserializer(faq)
        return Response(serializer.data)
    
    #특정FAQ게시글 수정
    elif request.method == 'PUT':
        serializer = Faqserializer(faq, data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    #특정FAQ게시글 삭제

    elif request.method == 'DELETE':
        fap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
