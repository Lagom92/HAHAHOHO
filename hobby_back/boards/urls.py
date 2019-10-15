from django.urls import path
from . import views


urlpatterns = [

    path('', views.postfree_list),
    path('<int:id>/', views.postfree_detail),

]