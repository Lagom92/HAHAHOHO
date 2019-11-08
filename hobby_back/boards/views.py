from django.shortcuts import redirect, get_object_or_404
from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from .models import PostHobby, PostFree, Faq, Notice, CommentFree, ParticipantCheck, User, CommentHobby, Bill
from .serializers import PostHobbySerializer, PostFreeSerializer, NoticeSerializer
from .serializers import FaqSerializer, CommentFreeSerializer, ParticipantCheckSerializer, CommentHobbySerializer


class postHobby_list(generics.ListCreateAPIView):
    '''
    취미 게시판 list page를 생성, 조회 하는 API

    ---
    ## `/boards/hobby`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - subclass: 카테고리 소분류
        - startDay: 모임 날짜
        - startTime: 모임 시간
        - endDay: 모임 모집 마감 날짜
        - gender: 모임 성별 여부
        - minAge: 희망 최소 연령
        - maxAge: 희망 최대 연령
        - member: 최대 인원
        - location: 모임을 할 장소
        - fee: 비용
        - photo: 이미지
    '''
    search_fields = ['title', 'contents', 'location']
    filter_backends = (filters.SearchFilter,)
    queryset = PostHobby.objects.all().order_by('-id')
    serializer_class = PostHobbySerializer
    
class postHobby_detail(generics.RetrieveUpdateDestroyAPIView):
    '''
    취미 게시판 detail page를 조회, 수정, 삭제 하는 API

    ---
    ## `/boards/hobby/{id}`
    ## 내용
       - title: 게시판 제목
        - contents: 게시판 내용
        - subclass: 카테고리 소분류
        - startDay: 모임 날짜
        - startTime: 모임 시간
        - endDay: 모임 모집 마감 날짜
        - gender: 모임 성별 여부
        - minAge: 희망 최소 연령
        - maxAge: 희망 최대 연령
        - member: 최대 인원
        - location: 모임을 할 장소
        - fee: 비용
        - photo: 이미지
    '''
    queryset = PostHobby.objects.all()
    serializer_class = PostHobbySerializer



class postFree_list(generics.ListCreateAPIView):
    '''
    자유 게시판 list page를 생성, 조회 하는 API
    
    ---
    ## `/boards/free`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - user: 게시판 작성자
        - created_at: 게시판 작성 날짜 및 시간
    '''
    search_fields = ['title', 'contents']
    filter_backends = (filters.SearchFilter,)
    queryset = PostFree.objects.all().order_by('-id')
    serializer_class = PostFreeSerializer

class postFree_detail(generics.RetrieveUpdateDestroyAPIView):
    '''
    자유 게시판 detail page를 조회, 수정, 삭제 하는 API
    
    ---
    ## `/boards/free/{id}`
    ## 내용
        - title: 게시판 제목
        - contents: 게시판 내용
        - user: 게시판 작성자
        - created_at: 게시판 작성 날짜 및 시간
    '''
    queryset = PostFree.objects.all()
    serializer_class = PostFreeSerializer

class notice_list(generics.ListAPIView):
    '''
    공지사항 게시판 list page를 조회 하는 API
    
    ---
    ## `/boards/notice`
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
    ## `/boards/notice/{id}`
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
    ## `/boards/faq`
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
    ## `/boards/faq/{id}`
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
    메인 페이지에서 보여주는 모임 목록들
    최신순으로 정렬, 최대 6개

    ---
    ## `/boards/main/hobby`

    '''
    queryset = PostHobby.objects.all().order_by('-id')[:6]
    serializer_class = PostHobbySerializer

class main_notice(generics.ListAPIView):
    '''
    메인 페이지에서 보여주는 공지사항들
    최신순으로 정렬, 최대 5개

    ---
    ## `/boards/main/notice`

    '''
    queryset = Notice.objects.all().order_by('-id')[:5]
    serializer_class = NoticeSerializer

class main_free(generics.ListAPIView):
    '''
    메인 페이지에서 보여주는 자유게시판들
    최신순으로 정렬, 최대 5개

    ---
    ## `/boards/main/free`

    '''
    queryset = PostFree.objects.all().order_by('-id')[:5]
    serializer_class = PostFreeSerializer

class commentFree_list(generics.CreateAPIView):
    '''
    자유게시판의 댓글 생성 기능

    ---

    '''
    queryset = CommentFree.objects.all()
    serializer_class = CommentFreeSerializer

@api_view(['GET'])
def comments(request, pk):
    '''
    자유게시판의 댓글 list 기능

    ---

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
    '''
    모임 목록에 유저 추가 및 삭제

    ---
    
    
    '''
    if request.method == 'POST':
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
            return Response(datas)
    elif request.method == 'DELETE':
        participant = ParticipantCheck.objects.get(post=post_id, user=user_id)

        participant.delete()
        return Response("delete success")
    else:
        raise NameError

@api_view(['GET'])
def participantCheckListByPost(request, post_id):
    '''
    포스트 이름으로 참여자 목록 찾기

    ---
    
    
    '''
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
    '''
    유저로 참가한 포스트 찾기

    ---
    
    
    '''
    participant = ParticipantCheck.objects.filter(user_id=user_id).values()
    posts = {}
    for idx, i in enumerate(participant):
        postId = participant[idx].get('post_id')
        post = PostHobby.objects.get(id=postId)
        serializer = PostHobbySerializer(post)
        posts['{}'.format(idx)] = serializer.data  
    return Response(posts)

@api_view(['POST'])
def refund(request, post_id, user_id):
    '''
    포인트 환불

    ---
    
    
    '''
    user = User.objects.get(id=user_id)
    postHobby = PostHobby.objects.get(id=post_id)
    point = 2000
    user.userPoint += point
    Bill.objects.create(
        user = user,
        money = point,
        postHobby = postHobby,
        change = "point 환불"
    )
    user.save()
    return Response("Refund complete")

@api_view(['POST'])
def pay(request, post_id, user_id):
    '''
    포인트 결제

    ---
    
    
    '''
    user = User.objects.get(id=user_id)
    postHobby = PostHobby.objects.get(id=post_id)
    point = 2000
    user.userPoint -= point
    Bill.objects.create(
        user = user,
        money = point,
        postHobby = postHobby,
        change = "point 차감"
    )
    user.save()
    return Response("Pay complete")

@api_view(['GET'])
def getBills(request, user_id):
    '''
    포인트 내역 조회

    ---
    
    
    '''
    queryset = Bill.objects.all().order_by('-id')
    queryset = queryset.filter(user_id = user_id)
    data = []
    for query in queryset:
        box={}
        if user_id == query.user.id:
            box['post_title'] = query.postHobby.title
            box['post_id'] = query.postHobby.id
            box['money'] = query.money
            box['change'] = query.change
            box['created_at'] = query.created_at
            data.append(box)
    return Response(data)


@api_view(['POST'])
def addCart(request, user_id):
    '''
    찜하기

    ---
    
    
    '''
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
    '''
    찜 내역 조회

    ---
    
    
    '''
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

    '''
    queryset = CommentHobby.objects.all()
    serializer_class = CommentHobbySerializer

@api_view(['GET'])
def hobbyComments(request, pk):
    '''
    모임 게시판의 댓글 list 기능

    ---

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

    '''
    commenthobby = get_object_or_404(CommentHobby, pk=pk)
    if request.method == 'GET':
        serializer = CommentHobbySerializer(commenthobby)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        commenthobby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)