from django.conf.urls import include, url
from .views import KakaoLogin, NaverLogin
from . import views

app_name = 'accounts'

urlpatterns = [
    url('rest-auth/kakao/',  KakaoLogin.as_view(), name='kakao_login'),
    url('rest-auth/naver/',  NaverLogin.as_view(), name='naver_login'),
    url('kakaoLogin/', views.Kakao_Login),
    url('naverLogin/', views.Naver_Login),
    url('kakaoPay/', views.kakaoPay),
    url('edit/<int:id>/', views.editUser),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)