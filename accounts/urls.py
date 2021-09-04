from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('login',views.login , name="login"),
    path('sign-up', views.sign_up, name="sign-up"),
    path('logout',views.Logout , name = "logout"),
]