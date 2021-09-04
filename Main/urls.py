from django.urls import path , include
from . import views
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.home , name='Home'),
    path('explore', views.explore, name='explore'),
    path('profile',views.profile,name='profile')
]

