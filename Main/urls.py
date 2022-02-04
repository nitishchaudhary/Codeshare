from django.urls import path , include
from django.http import request
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.home , name='Home'),
    path('explore', views.explore, name='explore'),
    path('trending',views.trending,name='trending'),
    path('projects',views.projects,name='projects'),
    path('search', views.search , name = 'search'),
    path('new-post' , views.post , name = 'post'),
    path('post/id:<int:pk>',views.post_detail , name = 'post-details'),
    path('post-comment/id:<int:pk>',views.comment , name='comment'),
    path('like-post/id:<int:pk>',views.like , name="like"),
    path('follow/user:<str:username>',views.follow_user , name="follow"),
    path('delete-post/id:<int:pk>',views.delete,name="delete"),
    path('share-project',views.share_project,name='share-project'),
    path('project/id:<int:pk>',views.show_project,name='show-project'),
    path('collab/id:<int:pk>',views.collab_request,name='collab_request'),
    path('collabs',views.collabs,name='collabs'),
    path('delete-notifications',views.delete_notifications,name='delete-notifications'),
    path('markall-read',views.mark_all_read,name='mark-all-read'),
]


