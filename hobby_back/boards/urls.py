from django.urls import path
from . import views

urlpatterns = [
    path('', views.postHobby_list),
    path('<int:pk>/', views.postHobby_detail),
    path('<int:id>/', views.postfree_detail),

]