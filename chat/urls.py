from django.urls import path
from . import views

urlpatterns=[
     path('',views.chats,name='chats'),
     path('user:<str:username>',views.chats,name='user-chat'),
     path('message/user:<str:username>',views.message,name='message'),
]