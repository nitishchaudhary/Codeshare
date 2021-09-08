from django.urls import path , include
from django.http import request
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.home , name='Home'),
    path('explore', views.explore, name='explore'),
]


