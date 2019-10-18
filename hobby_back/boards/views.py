from .models import PostHobby, PostFree, Faq, Notice
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer, FaqSerializer
from rest_framework import generics

<<<<<<< HEAD
from rest_framework import generics, filters

#취미게시판 

class Hobby_list(generics.ListCreateAPIView):
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer

# @api_view(['GET', 'POST'])
# def postHobby_list(request):
#     # Read
#     if request.method == 'GET':
#         queryset = PostHobby.objects.all()
#         serializer = PostHobbySerializer(queryset, many=True)
#         return Response(serializer.data)
#     # Create
#     elif request.method == 'POST':
#         serializer = PostHobbySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATE)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
=======
class postHobby_list(generics.ListCreateAPIView):
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer
>>>>>>> 695fc66a107b76842a4f152408fc2a177cf7b1ed

class postHobby_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer

class postFree_list(generics.ListCreateAPIView):
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

<<<<<<< HEAD
    # Delete
    elif request.method == 'DELETE':
        posthobby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#자유게시판
# generic으로 수정 중...
class Free_list(generics.ListCreateAPIView):
    queryset = PostFree.objects.all()
    serializer_class = PostFreeSerializer


# @api_view(['GET','POST'])
# def postFree_list(request):
#     #자유게시판 조회기능
#     if request.method == 'GET':
#         queryset = PostFree.objects.all()
#         serializer = PostFreeSerializer(queryset, many = True)
#         return Response(serializer.data)


#     #자유게시판 글 생성기능
#     elif request.method == 'POST':
#         serializer = PostFreeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATE)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def postFree_detail(request,id):

    # try/except code
    # try:
    #     postfree = PostFree.objects.get(id=id)
    # except PostFree.DoesNotExist:

    #     return Response(status= status.HTTP_404_NOT_FOUND)

    #get 404 short cut code
    postfree = get_object_or_404(PostFree, id=id)

    #특정 게시글 조회하기
    if request.method == 'GET':
        serializer = PostFreeSerializer(postfree)
        return Response(serializer.data)

    #특정 게시글 수정
    elif request.method == 'PUT':
        serializer = PostFreeSerializer(postfree, data=request.data)
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
        serializer = NoticeSerializer(queryset, many = True)
        return Response(serializer.data)

    #공지사항 글 생성 기능
    elif request.method == 'POST':
        serializer = NoticeSerializer(data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','DELETE'])
def notice_detail(request, id):
    #try/except code
    # try:
    #     notice = Notice.objects.get(id=id)
    # except Notice.DoesNotExist:
    #     return Response(status.HTTP__404_NOT_FOUND)

    #get 404 short cut code
    notice = get_object_or_404(Notice, id=id)

    

    #특정 공지사항글 조회하기

    if request.method == 'POST':
        serializer = NoticeSerializer(notice)
        return Response(serializer.data)

    #특정 공지사항 글 수정하기

    elif request.method == 'PUT':
        serializer = NoticeSerializer(notice, data= request.data)
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
        serializer = FaqSerializer(queryset, many=True)
        return Response(serializer.data)

    # FAQ게시판 글쓰기 기능

    elif request.method =='POST':
        serializer = FaqSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATE)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def faq_detail(request, id):
    #try/except code
    # try:
    #     faq = Faq.objects.get(id=id)
    # except Faq.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    #get 404 short code
    faq = get_object_or_404(Faq, id=id)

    
    #특정FAQ게시글 조회
    if request.method == 'GET':
        serializer = FaqSerializer(faq)
        return Response(serializer.data)
    
    #특정FAQ게시글 수정
    elif request.method == 'PUT':
        serializer = FaqSerializer(faq, data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    #특정FAQ게시글 삭제

    elif request.method == 'DELETE':
        fap.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
=======
class faq_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
>>>>>>> 695fc66a107b76842a4f152408fc2a177cf7b1ed
