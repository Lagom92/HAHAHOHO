from django.conf.urls import include, url
from .views import KakaoLogin, NaverLogin
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    url('rest-auth/kakao/',  KakaoLogin.as_view(), name='kakao_login'),
    url('rest-auth/naver/',  NaverLogin.as_view(), name='naver_login'),
    url('userSave/', views.userSave),
    url('userInfo/', views.userInfo),
    url('naverLogin/', views.Naver_Login),
    url('kakaoPay/', views.kakaoPay),
    url('edit/<int:id>/', views.editUser),
    path('follow/<int:pk>/', views.follow_detail),
    path('follow/', views.follow_list),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)