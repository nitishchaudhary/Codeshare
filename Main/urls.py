from django.urls import path , include
from django.http import request
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.home , name='Home'),
    path('explore', views.explore, name='explore'),
    path('trending',views.trending,name='trending'),
    path('search', views.search , name = 'search'),
    path('new-post' , views.post , name = 'post'),
    path('post/id:<int:pk>',views.post_detail , name = 'post-details'),
    path('post-comment/id:<int:pk>',views.comment , name='comment'),
    path('like-post/id:<int:pk>',views.like , name="like"),
    path('follow/user:<str:username>',views.follow_user , name="follow"),
]


