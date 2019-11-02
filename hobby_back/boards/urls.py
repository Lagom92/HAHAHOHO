from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('hobby', views.postHobby_list.as_view()),
    path('hobby/<int:pk>', views.postHobby_detail.as_view()),
    path('free', views.postFree_list.as_view()),
    path('free/<int:pk>', views.postFree_detail.as_view()),
    path('notice', views.notice_list.as_view()),
    path('notice/<int:pk>', views.notice_detail.as_view()),
    path('faq', views.faq_list.as_view()),
    path('faq/<int:pk>', views.faq_detail.as_view()),
    path('main/hobby', views.main_hobby.as_view()),
    path('main/notice', views.main_notice.as_view()),
    path('main/free', views.main_free.as_view()),
    path('free/<int:pk>/comment', views.commentFree_list.as_view()),
    path('free/<int:pk>/comments', views.comments),
    path('comment/<int:pk>', views.commentFree_detail),
    # 모임 게시판 댓글
    path('hobby/<int:pk>/comment', views.hobbyComment.as_view()),
    path('hobby/<int:pk>/comments', views.hobbyComments),
    path('hobbyComment/<int:pk>', views.hobbyComment_detail),
    path('participantCheck/<int:post_id>/<int:user_id>', views.participantCheck),
    path('participantCheckListByUser/<int:user_id>', views.participantCheckListByUser),
    path('participantCheckListByPost/<int:post_id>', views.participantCheckListByPost),
    path('cartList/<int:user_id>', views.CartList),
    path('cart/<int:user_id>', views.addCart),
]

urlpatterns = format_suffix_patterns(urlpatterns)
