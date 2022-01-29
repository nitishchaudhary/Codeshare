from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Main.models import Post,Like

# Create your views here.
@login_required
def user_profile(request, username):
    id = request.user.id
    user = User.objects.get(id=id)
    user0 = User.objects.get(username = username)

    posts = Post.objects.filter(user_name=user0)
    dc ={}
    for x in posts:
        try:
            Like.objects.get(user=user,post=x)
            dc[x]='true'
        except:
            dc[x]='false'
    return render(request,'profile.html' , {'user0':user0,'posts':dc})

@login_required
def edit_profile(request, username):
    if username == request.user.username:
        return render(request, 'edit-profile.html')
    else:
        return HttpResponse("invalid action")