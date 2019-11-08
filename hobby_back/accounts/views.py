from django.shortcuts import redirect, get_object_or_404
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests, json
from .serializers import UserSerializer
from .models import User, payInfo, KakaoBill


class KakaoLogin(SocialLoginView):
    '''
    카카오 로그인

    ---
    
    
    '''
    adapter_class = KakaoOAuth2Adapter    

class NaverLogin(SocialLoginView):
    '''
    네이버 로그인

    ---
    
    
    '''
    adapter_class = NaverOAuth2Adapter

@api_view(['POST'])
def userInfo(request):
    '''
    유저 정보 가져오기

    ---
    
    
    '''
    userId = request.data.get('id')
    if userId[0] == "k" or userId[0] == "n":
        userSet = User.objects.get(userId=userId)
    else:
        userSet = User.objects.get(pk=userId)
    serializer = UserSerializer(userSet)
    return Response(serializer.data)

@api_view(['POST'])
def userSave(request):
    '''
    로그인시 유저 정보 저장

    ---
    
    
    '''
    userName = request.data.get('userName')
    userNickName = request.data.get("nickname")
    userId = request.data.get('userId')
    userSex = request.data.get('userSex')
    userAge = request.data.get("userAge")
    userImage = request.data.get('userImage')
    try: 
        userSet = User.objects.get(userId=userId)
        userSet.userImage = userImage
        userSet.save()
    except:
        User.objects.create(
            userName=userName, userNickName=userName, userSex=userSex, userAge=userAge, userImage=userImage, userId=userId
        )
    return Response("database save")


@api_view(['POST'])
def editUser(request, id):
    '''
    유저 정보 수정

    ---
    
    
    '''
    user = User.objects.get(id=id)
    if request.data.get('userAddress'):
        user.userAddress = request.data.get('userAddress')
        user.userGrade += 1
    user.userNickName = request.data.get('userNickName')
    if request.data.get('userLike'):
        user.userLike = request.data.get('userLike')
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data)
 
@api_view(['GET'])
def Naver_Login(request):
    '''
    네이버 로그인

    ---
    
    
    '''
    deploy = "http://54.180.148.99"
    code = request.GET.get('code')
    state = request.GET.get('state')
    clientId = 'IaquHgHTmPlf_gc_a8es'
    secretId = 'nUsvfl0B6c'
    apiUrl = "https://nid.naver.com/oauth2.0/token?grant_type=authorization_code&"
    apiUrl += "client_id=" + clientId + "&client_secret=" + secretId + "&code=" + str(code) + "&state=" + str(state)
    response = requests.get(apiUrl)
    response = json.loads(response.text)
    access_token = response.get('access_token')
    refresh_token = response.get('refresh_token')
    body = {
        'access_token': access_token,
        'code': code,
    }
    auth_response = requests.post("http://127.0.0.1:8000/accounts/rest-auth/naver/", data=body)
    auth_response = json.loads(auth_response.text)
    redirect_url = deploy
    redirect_url += "?jwt=" + auth_response.get('token')

    headers = {
        'Authorization':'Bearer ' + access_token
    }
    profile_url = "https://openapi.naver.com/v1/nid/me"
    profile_response = requests.get(profile_url, headers=headers)
    profile_response = json.loads(profile_response.text)
    userName = profile_response.get("response").get("name")
    userNickName = profile_response.get("response").get("nickname")
    userId = "naver_" + str(profile_response.get("response").get("id"))
    userSex = profile_response.get("response").get("gender")
    userAge = profile_response.get("response").get('age')
    userImage = profile_response.get("response").get("profile_image")
    try: 
        userSet = User.objects.get(userId=userId)
    except:
        User.objects.create(
            userName=userName, userNickName=userName, userSex=userSex, userAge=userAge, userImage=userImage, userId=userId
        )
    userSet = User.objects.values().filter(userId=userId)
    serializer = UserSerializer(userSet)
    ids = userSet.get().get('id')
    redirect_url += "&id="+str(ids)
    return redirect(redirect_url)
    
@api_view(['POST'])
def kakaoPay(request):
    '''
    카카오 페이 결제

    ---
    
    
    '''
    url = "https://kapi.kakao.com"
    front_url = "http://54.180.148.99"

    headers = {
        'Authorization': "KakaoAK " + "25f3b072b7bff63ee9a201aa1f5dc9d6",
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    user_id = int(request.data.get('userId'))
    params = {
        'cid': "TC0ONETIME",
        'partner_order_id': '1001',
        'partner_user_id': '',
        'item_name': '포인트',
        'quantity': 1,
        'total_amount': 0,
        'vat_amount': 200,
        'tax_free_amount': 0,
        'approval_url': front_url+'/user',
        'fail_url': front_url,
        'cancel_url': front_url,
    }
    params['partner_user_id'] = user_id
    params['total_amount'] = request.data.get('amount')
    response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
    response = json.loads(response.text)
    user = User.objects.get(id=user_id)
    if response.get('code'):
        raise NameError
    else:
        payInfo.objects.create(
            user=user, payNum=response.get('tid'), 
            payAmount=request.data.get('amount'), payDate=response.get('created_at')
        )
        KakaoBill.objects.create(
            user = user,
            money = request.data.get('amount'),
            change = "Kakao pay 충전"
        )
        user.userPoint += int(request.data.get('amount'))
        user.save()
        return Response(response)

@api_view(['GET'])
def getBills(request, user_id):
    '''
    카카오 페이 충전 내역 조회

    ---
    
    
    '''
    queryset = KakaoBill.objects.all().order_by('-id')
    queryset = queryset.filter(user_id = user_id)
    data = []
    for query in queryset:
        box={}
        if user_id == query.user.id:
            box['money'] = query.money
            box['change'] = query.change
            box['created_at'] = query.created_at
            data.append(box)
    return Response(data)

@api_view(['POST']) 
def following(request, meId, youId):
    '''
    팔로잉

    ---
    
    
    '''
    user = User.objects.get(id=meId)
    you = User.objects.get(id=youId)
    if user != you:
        if you in user.followings.all():
            user.followings.remove(you)
        else:
            user.followings.add(you)
    
    return Response("follow success") 

@api_view(['GET'])
def follows(request, id):
    '''
    팔로워

    ---
    
    
    '''
    user = User.objects.get(id=id)
    follows = user.followings.all().order_by('id')
    data = []
    for follow in follows:
        box={}
        box['id'] = follow.id
        box['name'] = follow.userNickName
        if follow.userImage == 'undefined':
            box['img'] = None
        else:
            box['img'] = str(follow.userImage)
        data.append(box)
    return Response(data)

@api_view(['GET'])
def followers(requets, id):
    '''
    팔로워

    ---
    
    
    '''
    me = User.objects.get(id=id)
    data = []
    print(me.userName)
    user = User.objects.all().order_by('id')
    for i in user:
        if me.userName != i.userName:
            box = {}
            flag = 0
            follower = i.followings.all()
            for j in follower:
                if j.userName == me.userName:
                    flag = 1
                    box['id'] = i.id
                    box['name'] = i.userName
                    if i.userName == 'undefined':
                        box['img'] = None
                    else:
                        box['img'] = str(i.userImage)
                    break
            if flag:
                data.append(box)
    return Response(data)