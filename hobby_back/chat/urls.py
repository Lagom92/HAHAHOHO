from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('<str:room_name>/', views.room),
]