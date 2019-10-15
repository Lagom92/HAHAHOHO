from django.conf.urls import include, url
from .views import KakaoLogin, NaverLogin

app_name = 'accounts'

urlpatterns = [
    url('rest-auth/kakao/',  KakaoLogin.as_view(), name='kakao_login'),
    url('rest-auth/naver/',  NaverLogin.as_view(), name='naver_login'),
]