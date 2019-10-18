from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
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
    print(response)
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    userName = response.get("properties").get("nickname")
    # userSex = response.get("gender")
    # userAge = response.get("age_range")
    userSex = "남자"
    userAge = 20
    userImage = response.get("")
    try: 
        userSet = User.objects.get(userName=userName)
    except:
        User.objects.create(
            userName=userName, userSex=userSex, userAge=userAge, userImage=userImage
        )
    userSet = User.objects.get(userName=userName)
    serializer = UserSerializer(userSet)
    return Response(serializer.data)

@api_view(['POST'])
def Naver_Login(request):
    pass
    # user_url = "https://kapi.kakao.com/v2/user/me"
    # user_headers = {
    #     'Authorization' : "Bearer " + request.data['access_token'],
    #     'Content-Type': 'application/json; charset=utf-8'
    # }
    # response = requests.post(user_url, headers=user_headers)
    # response = json.loads(response.text)
    # print(response)
    # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    # userName = response.get("properties").get("nickname")
    # # userSex = response.get("gender")
    # # userAge = response.get("age_range")
    # userSex = "남자"
    # userAge = 20
    # userImage = response.get("")
    # try: 
    #     userSet = User.objects.get(userName=userName)
    # except:
    #     User.objects.create(
    #         userName=userName, userSex=userSex, userAge=userAge, userImage=userImage
    #     )
    # userSet = User.objects.get(userName=userName)
    # serializer = UserSerializer(userSet)
    # return Response(serializer.data)
