from operator import truediv
from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Main.models import Post,Like,UserFollowing
from Main.views import get_notifications
# Create your views here.
@login_required
def user_profile(request, username):
    id = request.user.id
    user = User.objects.get(id=id)
    user0 = User.objects.get(username = username)    
    posts = Post.objects.filter(user_name=user0).order_by('-date_posted')
    dc ={}
    try:
        UserFollowing.objects.get(user_id=user,following_user_id=user0)
        following = 'true'
    except:
        following = 'false'

    for x in posts:
        user2 = User.objects.get(username=x.user_name)
        try:
            like = Like.objects.get(user=user,post=x)
            dc[x] = 'liked'
        except:
            dc[x] = 'notliked'
    
    notifications,count = get_notifications(id)
    return render(request,'profile.html' , {'user0':user0,'following':following,'posts':dc,'notifications':notifications,'count':count})

@login_required
def edit_profile(request, username):
    if username == request.user.username:
        id = request.user.id
        notifications,count = get_notifications(id)
        return render(request, 'edit-profile.html',{'notifications':notifications,'count':count})
    else:
        return HttpResponse("invalid action")