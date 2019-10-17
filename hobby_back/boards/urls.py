from django.urls import path
from . import views

urlpatterns = [
    path('hobby/', views.postHobby_list),
    path('free/', views.postFree_list),
    path('notice/', views.notice_list),
    path('faq/', views.faq_list),
    path('hobby/<int:id>/', views.postHobby_detail),
    path('free/<int:id>/', views.postFree_detail),
    path('notice/<int:id>/', views.notice_detail),
    path('faq/<int:id>/', views.faq_detail),
]