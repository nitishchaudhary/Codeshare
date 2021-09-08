from django.urls import path , include
from django.http import request
from . import views
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.home , name='Home'),
    path('explore', views.explore, name='explore'),
    path('user-<str:username>',views.profile,name='profile'),
    path('edit-profile',views.edit_profile , name='edit-profile')
]


