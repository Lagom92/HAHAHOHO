from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PostHobby, PostFree
from .serializers import PostHobbySerializer, PostFreeserializer


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
def postHobby_detail(request, pk):
    try:
        postHobby = PostHobby.objects.get(pk=pk)
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


@api_view(['GET','POST'])
def postfree_list(request):
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
def postfree_detail(request,id):
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
