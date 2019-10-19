from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, payInfo
from .serializers import UserSerializer
import requests, json



class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter    
    '''
    1. access token을 넣어서 리턴받은 jwt 토큰을 가져오기
    2. 가져온 토큰으로 https://kapi.kakao.com/v2/user/me 에 요청보내기
    3. 리턴받은 정보를 db에 저장하기
    '''    

class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter


@api_view(['POST'])
def Kakao_Login(request):
    user_url = "https://kapi.kakao.com/v2/user/me"
    user_headers = {
        'Authorization' : "Bearer " + request.data['access_token'],
        'Content-Type': 'application/json; charset=utf-8'
    }
    response = requests.post(user_url, headers=user_headers)
    response = json.loads(response.text)
    userName = response.get("properties").get("nickname")
    userNickName = response.get("properties").get("nickname")
    # userSex = response.get("gender")
    # userAge = response.get("age_range")
    userSex = "남자"
    userAge = 20
    userImage = response.get("properties").get("profile_image")
    try: 
        userSet = User.objects.get(userName=userName)
    except:
        User.objects.create(
            userName=userName, userNickName=userName, userSex=userSex, userAge=userAge, userImage=userImage
        )
    userSet = User.objects.get(userName=userName)
    serializer = UserSerializer(userSet)
    return Response(serializer.data)



@api_view(['POST'])
def editUser(request):
    # 유저 프로필 수정
    ## 이미지
    ## 주소
    ## 선호 카테고리
    ## 닉네임
    pass

@api_view(['POST'])
def Naver_Login(request):
    pass



@api_view(['POST'])
def kakaoPay(request):
    # request에 회원 id, 결제가격을 같이 보내줘야 함 : db에 결제정보를 저장하기 위해서
    url = "https://kapi.kakao.com"
    headers = {
        'Authorization': "KakaoAK " + "25f3b072b7bff63ee9a201aa1f5dc9d6",
        'Content-type': 'application/x-www-form-urlencoded;charset=utf-8',
    }
    params = {
        'cid': "TC0ONETIME",
        'partner_order_id': '1001',
        # 주문자 정보 id
        'partner_user_id': 'dongsik',
        'item_name': '포인트',
        'quantity': 1,
        # 결제 금액
        'total_amount': 0,
        'vat_amount': 200,
        'tax_free_amount': 0,
        'approval_url': 'http://localhost:8080',
        'fail_url': 'http://localhost:8080',
        'cancel_url': 'http://localhost:8080',
    }
    # params['partner_user_id'] = reqeust.data.get('userId')
    params['total_amount'] = request.data.get('amount')
    response = requests.post(url+"/v1/payment/ready", params=params, headers=headers)
    response = json.loads(response.text)
    if(response.get('code')):
        # 에러일때 
        pass
    else:
        # 에러가 아닐 때
        # db저장
        # payInfo.objects.create(
        #     user=request.data.get('userId'), payNum=response.get('tid'), 
        #     payAmount=request.data.get('amount'), payDate=response.get('created_at')
        # )
        return Response(response)
    print(response)
    