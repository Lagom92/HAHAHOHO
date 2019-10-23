from django.conf.urls import include
from django.urls import path
from .views import KakaoLogin, NaverLogin
from . import views

app_name = 'accounts'

urlpatterns = [
    path('rest-auth/kakao/',  KakaoLogin.as_view(), name='kakao_login'),
    path('rest-auth/naver/',  NaverLogin.as_view(), name='naver_login'),
    path('userSave/', views.userSave),
    path('userInfo/', views.userInfo),
    path('naverLogin/', views.Naver_Login),
    path('kakaoPay/', views.kakaoPay),
    path('edit/<int:id>/', views.editUser),
    path('follow/<int:pk>/', views.follow_detail),
    path('follow/', views.follow_list),
]
