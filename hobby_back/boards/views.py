from django.shortcuts import redirect, get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import PostHobby, PostFree, Faq, Notice, CommentFree, ParticipantCheck, User, CommentHobby
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer
from .serializers import FaqSerializer, CommentFreeSerializer, ParticipantCheckSerializer, CommentHobbySerializer

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
    queryset = PostHobby.objects.all().order_by('-id')
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
    queryset = PostFree.objects.all().order_by('-id')
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
    queryset = Notice.objects.all().order_by('-id')
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
    queryset = Notice.objects.all().order_by('-id')
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
    queryset = Faq.objects.all().order_by('-id')
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

class main_hobby(generics.ListAPIView):
    '''
    메인 페이지에서 보여주는 모임들
    최근 만들어진 순으로 정렬
    최대 6개

    ---
    ## 내용

    '''
    queryset = PostHobby.objects.all().order_by('-id')[:6]
    serializer_class = PostHobbySerializer

class main_notice(generics.ListAPIView):
    '''
    메인 페이지에서 보여주는 모임들
    최근 만들어진 순으로 정렬
    최대 6개

    ---
    ## 내용

    '''
    queryset = Notice.objects.all().order_by('-id')[:5]
    serializer_class = NoticeSerializer

class main_free(generics.ListAPIView):
    '''
    메인 페이지에서 보여주는 모임들
    최근 만들어진 순으로 정렬
    최대 6개

    ---
    ## 내용

    '''
    queryset = PostFree.objects.all().order_by('-id')[:5]
    serializer_class = PostFreeSerializer

class commentFree_list(generics.CreateAPIView):
    '''
    자유게시판의 댓글 생성 기능

    ---
    ## 내용

    '''
    queryset = CommentFree.objects.all()
    serializer_class = CommentFreeSerializer

@api_view(['GET'])
def comments(request, pk):
    '''
    자유게시판의 댓글 list 기능

    ---
    ## 내용

    '''
    queryset = CommentFree.objects.all().order_by('-id')
    queryset = queryset.filter(postFree_id = pk)
    data = []
    for query in queryset:
        box = {}
        box['id'] = query.id
        box['user'] = query.user.id
        box['name'] = query.user.userName
        box['contents'] = query.contents
        box['created_at'] = query.created_at
        data.append(box)
    return Response(data)

@api_view(['GET', 'DELETE'])
def commentFree_detail(request, pk):
    '''
    자유게시판의 댓글 detail, delete 기능

    ---
    ## 내용

    '''
    commentfree = get_object_or_404(CommentFree, pk=pk)
    if request.method == 'GET':
        serializer = CommentFreeSerializer(commentfree)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        commentfree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST',  'DELETE'])
def participantCheck(request, post_id, user_id):
    if request.method == 'POST':
        # post요청이면 모임목록에 유저 추가  
        try:
            ParticipantCheck.objects.get(post=post_id, user=user_id)          
            return Response("이미 모임에 존재하는 유저입니다")
        except:
            user = User.objects.get(id=user_id)
            post = PostHobby.objects.get(id=post_id)
            cart = post.cart.filter(id=user_id)
            img = user.userImage
            nickName = user.userNickName
            if user in cart:
                post.cart.remove(user)
            participant = ParticipantCheck.objects.create(
                post=post, user=user
            )
            datas = {
                'user_id': user_id,
                'user_name': nickName,
                'user_image': str(img)
            }
            # return Response("{}".format(datas))
            return Response(datas)
    elif request.method == 'DELETE':
        # delete요청이면 해당 모임에 대해 취소 신청을 했기 때문에 해당 유저 삭제
        participant = ParticipantCheck.objects.get(post=post_id, user=user_id)
        participant.delete()
        return Response("delete success")
    else:
        raise NameError

@api_view(['GET'])
def participantCheckListByPost(request, post_id):
    # 포스트 이름으로 참여자 목록 찾기
    participant = ParticipantCheck.objects.filter(post_id=post_id).values()
    user_groups = {
        'user_group' : []
    }
    for i in participant:
        user = User.objects.get(id=i.get('user_id'))
        user_groups['user_group'].append({
            'user_id':i.get('user_id'),
            'user_name':user.userName,
            'user_image':str(user.userImage)
            })
    return Response(user_groups)

@api_view(['GET'])
def participantCheckListByUser(request, user_id):
    # 유저로 참가한 포스트 찾기
    participant = ParticipantCheck.objects.filter(user_id=user_id).values()
    posts = {}
    for idx, i in enumerate(participant):
        postId = participant[idx].get('post_id')
        post = PostHobby.objects.get(id=postId)
        serializer = PostHobbySerializer(post)
        posts['{}'.format(idx)] = serializer.data  
    return Response(posts)

@api_view(['POST'])
def addCart(request, user_id):
    user = User.objects.get(id=user_id)
    post_id = request.data.get('post_id')
    post = PostHobby.objects.get(id=post_id)
    cart = post.cart.all()
    if user in cart:
        post.cart.remove(user)
        return Response("undefined")
    else:
        post.cart.add(user)
        return Response(0)

@api_view(['GET'])
def CartList(request, user_id):
    # print(request.data)
    user = User.objects.get(id=user_id)
    post = PostHobby.objects.all()
    post_group = {'post_id':[]}
    for i in post:
        cart = i.cart.all()
        for j in cart:
            if(user == j):
                post_group['post_id'].append(i.id) 
    return Response(post_group)

# 모임 게시판 댓글
class hobbyComment(generics.CreateAPIView):
    '''
    모임 게시판의 댓글 생성 기능

    ---
    ## 내용

    '''
    queryset = CommentHobby.objects.all()
    serializer_class = CommentHobbySerializer

@api_view(['GET'])
def hobbyComments(request, pk):
    '''
    모임 게시판의 댓글 list 기능

    ---
    ## 내용

    '''
    queryset = CommentHobby.objects.all().order_by('-id')
    queryset = queryset.filter(postHobby_id = pk)
    data = []
    for query in queryset:
        box = {}
        box['id'] = query.id
        box['user'] = query.user.id
        box['name'] = query.user.userName
        box['contents'] = query.contents
        box['created_at'] = query.created_at
        data.append(box)
    return Response(data)

@api_view(['GET', 'DELETE'])
def hobbyComment_detail(request, pk):
    '''
    모임 게시판의 댓글 detail, delete 기능

    ---
    ## 내용

    '''
    commenthobby = get_object_or_404(CommentHobby, pk=pk)
    if request.method == 'GET':
        serializer = CommentHobbySerializer(commenthobby)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        commenthobby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)