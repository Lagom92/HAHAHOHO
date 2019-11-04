from django.conf.urls import include
from django.urls import path
from .views import KakaoLogin, NaverLogin
from . import views

app_name = 'accounts'

urlpatterns = [
    path('rest-auth/kakao',  KakaoLogin.as_view(), name='kakao_login'),
    path('rest-auth/naver',  NaverLogin.as_view(), name='naver_login'),
    path('userSave', views.userSave),
    path('userInfo', views.userInfo),
    path('naverLogin', views.Naver_Login),
    path('kakaoPay', views.kakaoPay),
    path('user/<int:id>', views.editUser),
    path('fame', views.fame_update),
    path('following/<int:meId>/<int:youId>', views.following),
    path('follows/<int:id>', views.follows),
    path('followers/<int:id>', views.followers),
    # path('cart/<int:user_id>/<int:post_id>', views.Cart),
    # path('cartList/<int:user_id>', views.CartList),
    path('bill/<int:user_id>', views.getBills),
]
