from django.urls import path
from . import consumers

websocket_urlpatterns =[
     path('chats/',consumers.ChatConsumer.as_asgi(),),
     path('chats/user:<str:username>',consumers.ChatConsumer.as_asgi(),),
]