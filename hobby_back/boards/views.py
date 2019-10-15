from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PostHobby
from .serializers import PostHobbySerializer

@api_view(['GET', 'POST'])
def postHobby_lpoist(request):
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