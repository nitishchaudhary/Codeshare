from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def user_profile(request, username):
    user0 = User.objects.get(username = username)
    return render(request,'profile.html' , {'user0':user0})

@login_required
def edit_profile(request, username):
    if username == request.user.username:
        return render(request, 'edit-profile.html')
    else:
        return HttpResponse("invalid action")