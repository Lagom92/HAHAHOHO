from django.urls import path
from . import views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from boards import views

urlpatterns = [
    path('hobby/', views.postHobby_list.as_view()),
    path('free/', views.postFree_list.as_view()),
    path('notice/', views.notice_list.as_view()),
    path('faq/', views.faq_list.as_view()),
    path('hobby/<int:id>/', views.postHobby_detail.as_view()),
    path('free/<int:id>/', views.postFree_detail.as_view()),
    path('notice/<int:id>/', views.notice_detail.as_view()),
    path('faq/<int:id>/', views.faq_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
