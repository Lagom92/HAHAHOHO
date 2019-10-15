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
