from django.urls import path
from . import views

urlpatterns = [
    path('hobby/', views.postHobby_list),
    path('hobby/<int:id>/', views.postHobby_detail),

    path('free/', views.postFree_list),
    path('free/<int:id>/', views.postFree_detail),

    path('notice/', views.notice_list),
    path('notice/<int:id>/', views.notice_detail),

    path('faq/', views.faq_list),
    path('faq/<int:id>/', views.faq_detail),
    


]