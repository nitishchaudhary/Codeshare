from ast import And, Or
from datetime import date
from itertools import count
from pickle import TRUE
import re
from typing import Type
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile , Post, Project_tag, like_project ,notification, Comment , Like ,like_project,project_comment, UserFollowing,Message,Project,collab
import json
from django.db.models import Q,Count
from django.core import serializers
from accounts.views import update
# Create your views here.

def get_notifications(id):
    usr = User.objects.get(id=id)
    all_notificaions = notification.objects.filter(user_id = usr).order_by('-notification_time')
    count = all_notificaions.filter(read = False).count()
    return all_notificaions,count

def delete_notifications(request):
    id = request.user.id
    usr = User.objects.get(id=id)
    try:
        notification.objects.filter(user_id = usr).delete()
        return HttpResponse("No Notifications")
    except:
        return HttpResponse('invalid command')

def mark_all_read(request):
    id = request.user.id
    usr = User.objects.get(id=id)
    notifications = notification.objects.filter(user_id = usr, read = False)
    for noti in notifications:
        noti.read = True
        noti.save()
    return HttpResponse('success')

def welcome(request):
    id = request.user.id
    user = User.objects.get(id=id)
    if request.method == 'GET':
        try:
            user_following = UserFollowing.objects.filter(user_id=user)
            users =[]
            for x in user_following:
                users.append(x.following_user_id)
            users_to_follow = User.objects.exclude(username__in = users).exclude(username = user)
        except: 
            users_to_follow = User.objects.all()
        return render(request,'welcome.html',{'users_to_follow':users_to_follow})
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        about = request.POST['about']
        if 'image' in request.FILES:
            image = request.FILES['image']
            user.profile.pic = image
        user.first_name= firstname
        user.last_name = lastname
        user.profile.about = about
        user.save()
        return redirect('/')

def home(request):
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        user_following = UserFollowing.objects.filter(user_id=user)
        users =[]
        for x in user_following:
            users.append(x.following_user_id) 
        dc ={}
        post = Post.objects.filter(Q(user_name__in = users) | Q(user_name=user)).order_by('-date_posted')
        # post = Post.objects.all().order_by('-date_posted')
        for x in post:
            user2 = User.objects.get(username=x.user_name)
            try:
                like = Like.objects.get(user=user,post=x)
                try:
                    UserFollowing.objects.get(user_id=user,following_user_id=user2)
                    a = {"liked":'true',"following":'true'}
                    dc[x] = a
                except:
                    a = {"liked":'true',"folllowing":'false'}
                    dc[x] = a
            except:
                try:
                    UserFollowing.objects.get(user_id=user,following_user_id=user2)
                    a = {"liked":'false',"following":'true'}
                    dc[x] = a
                except:
                    a = {"liked":'false',"folllowing":'false'}
                    dc[x] = a


        user_to_follow = User.objects.exclude(username__in = users).exclude(username = user)
        notifications,count= get_notifications(id)

        return render(request, 'explore.html',{'post':dc,'user_to_follow':user_to_follow,'notifications':notifications,'count':count})
    else:
        return render(request,'home.html')

def explore(request):
    return render(request,'explore.html')

def trending(request):
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        user_following = UserFollowing.objects.filter(user_id=user)
        users =[]
        for x in user_following:
            users.append(x.following_user_id) 
        posts = Post.objects.annotate(like_count=Count('likes')).order_by('-like_count')  
        dc ={}
        for x in posts:
            user2 = User.objects.get(username=x.user_name)
            try:
                like = Like.objects.get(user=user,post=x)
                try:
                    UserFollowing.objects.get(user_id=user,following_user_id=user2)
                    a = {"liked":'true',"following":'true'}
                    dc[x] = a
                except:
                    a = {"liked":'true',"folllowing":'false'}
                    dc[x] = a
            except:
                try:
                    UserFollowing.objects.get(user_id=user,following_user_id=user2)
                    a = {"liked":'false',"following":'true'}
                    dc[x] = a
                except:
                    a = {"liked":'false',"folllowing":'false'}
                    dc[x] = a
        user_to_follow = User.objects.exclude(username__in = users).exclude(username = user)
        notifications,count= get_notifications(id)

        return render(request,'trending.html',{'posts':dc,'notifications':notifications,'count':count,'user_to_follow':user_to_follow})

def projects(request):
    id = request.user.id
    user = User.objects.get(id=id)
    user_following = UserFollowing.objects.filter(user_id=user)
    users =[]
    for x in user_following:
        users.append(x.following_user_id)
    user_to_follow = User.objects.exclude(username__in = users).exclude(username = user)
    projects = Project.objects.all().order_by('-project_date')
    dc={}
    for x in projects:
        user2 = User.objects.get(username=x.author_id)
        try:
            like = like_project.objects.get(user_id=user,project=x)
            try:
                UserFollowing.objects.get(user_id=user,following_user_id=user2)
                a = {"liked":'true',"following":'true'}
                dc[x] = a
            except:
                a = {"liked":'true',"folllowing":'false'}
                dc[x] = a
        except:
            try:
                UserFollowing.objects.get(user_id=user,following_user_id=user2)
                a = {"liked":'false',"following":'true'}
                dc[x] = a
            except:
                a = {"liked":'false',"folllowing":'false'}
                dc[x] = a
    notifications,count = get_notifications(id)
    
    return render(request,'projects.html',{'projects':dc,'notifications':notifications,'count':count,'user_to_follow':user_to_follow})

def project_like(request,pk):
    id = request.user.id
    usr = User.objects.get(id=id)
    project = Project.objects.get(pk=pk)
    liked = False
    try:
        like = like_project.objects.get(user_id=usr , project=project).delete()

    except:
        liked = True
        like = like_project.objects.create(user_id=usr , project=project)
        like.save()
        # push notification
        user = project.author_id
        if user !=  usr:
            mssg = f"{usr.username} liked your project idea"
            notify = notification.objects.create(user_id = user,notification_from=usr, notification_message = mssg)
            notify.save()
    res = {
        'liked':liked
    }
    response = json.dumps(res)
    return HttpResponse(response,content_type="application/json")

def comment_project(request,pk):    
    if request.method == "POST":
        id = request.user.id
        project = Project.objects.get(pk = pk)
        user = User.objects.get(id = id)
        comment_data = request.POST['comment']
        comment = project_comment.objects.create(project = project , user_id = user , comment = comment_data)
        comment.save()
        
        # push notification
        usr = project.author_id
        print(usr)
        mssg = f"{user.username} commented on your project idea"
        notify = notification.objects.create(user_id = usr ,notification_from=user,notification_message = mssg )
        notify.save()

        return HttpResponse('done')


def search(request):
    id = request.user.id
    usr = User.objects.get(id=id)
    if request.GET.get('search'):
        keyword = request.GET['search']
        user =User.objects.all()
        tag_objects = Project_tag.objects.filter(tag = keyword)
        projects=[]
        for x in tag_objects:
            projects.append(x.project)
        found_users = {}
        for i in user:
            if keyword == i.username or i.first_name == keyword:
                try:
                    x = UserFollowing.objects.get(user_id=usr,following_user_id = i)
                    found_users[i] = 'true'
                except:
                    found_users[i] = 'false'
                    
                
        notifications,count= get_notifications(id)
        return render(request , "search_results.html" , {'users':found_users,'projects':projects,'notifications':notifications,'count':count})

def post(request):
    id = request.user.id
    user = User.objects.get(id = id)   
    des = request.POST['des']
    if 'post_image' in request.FILES:
        image = request.FILES['post_image']   
        post = Post.objects.create(user_name = user , description = des ,img = image)
    else:
        post = Post.objects.create(user_name = user , description = des)
    post.save()
    return redirect('/')
        
def post_detail(request,pk):
    id = request.user.id
    user = User.objects.get(id=id)
    user_following = UserFollowing.objects.filter(user_id=user)
    users =[]
    for x in user_following:
        users.append(x.following_user_id) 
    post = Post.objects.get(pk=pk)
    user2 = User.objects.get(username = post.user_name)
    try:
        check_following = UserFollowing.objects.get(user_id = user,following_user_id=user2)
        following = 'true'
    except:
        following = 'false'

    try:
        like = Like.objects.get(user=user , post=post)
        liked = 'true'
                    
    except:
        liked = 'false'

    user_to_follow = User.objects.exclude(username__in = users).exclude(username = user)
    notifications,count= get_notifications(id)

    return render(request, 'post.html',{'post':post,'liked':liked,'following':following,'user_to_follow':user_to_follow,'notifications':notifications,'count':count})

    # return render(request,'post.html',{'post':post})

def comment(request,pk):    
    if request.method == "POST":
        id = request.user.id
        post = Post.objects.get(pk = pk)
        user = User.objects.get(id = id)
        comment_data = request.POST['comment']
        comment = Comment.objects.create(post = post , username = user , comment = comment_data)
        comment.save()
        
        # push notification
        usr = post.user_name
        print(usr)
        mssg = f"{user.username} commented on your post"
        notify = notification.objects.create(user_id = usr ,notification_from=user,notification_message = mssg )
        notify.save()

        return HttpResponse('done')
        
def like(request,pk):
    id = request.user.id
    usr = User.objects.get(id=id)
    post = Post.objects.get(pk=pk)
    liked = False
    try:
        like = Like.objects.get(user=usr , post=post).delete()

    except:
        liked = True
        like = Like.objects.create(user=usr , post=post)
        like.save()
        # push notification
        user = post.user_name
        if user != usr:
            mssg = f"{usr.username} liked your post"
            notify = notification.objects.create(user_id = user, notification_message = mssg,notification_from = usr)
            notify.save()
    res = {
        'liked':liked
    }
    response = json.dumps(res)
    return HttpResponse(response,content_type="application/json")

def delete(request,pk):
    id = request.user.id
    user = User.objects.get(id=id)
    post = Post.objects.get(pk=pk)
    if(post.user_name == user):
        post.delete()
        return redirect('/')
    else:
        return HttpResponse("Invalid url")


def follow_user(request,username):    
    id = request.user.id
    usr = User.objects.get(id = id)
    usr2 = User.objects.get(username = username)
    try:
        obj = UserFollowing.objects.get(user_id = usr , following_user_id = usr2).delete()
        print("unfollowed")
        # push notification
        mssg = f"{usr.username} just unfollowed you"
        notify = notification.objects.create(user_id = usr2,notification_from=usr, notification_message = mssg)

    except:
        obj = UserFollowing.objects.create(user_id = usr , following_user_id = usr2)
        print("followed")
        obj.save()
        
        # push notification
        mssg = f"{usr.username} just followed you"
        notify = notification.objects.create(user_id = usr2,notification_from=usr,notification_message = mssg)
        notify.save()
    if 'welcome' in request.GET:
        return HttpResponse('done')
    else:
        return redirect('/')

def share_project(request):
    if request.method == 'POST':
        id=request.user.id
        usr = User.objects.get(id=id)
        title = request.POST['project-title']
        desc = request.POST['project-description']

        if request.POST['project-link']:
            link = request.POST['project-link']
            project = Project.objects.create(author_id=usr,title=title,description=desc,link=link)

        else:
            project = Project.objects.create(author_id=usr,title=title,description=desc)

        project.save()
        if  request.POST.getlist('tag'):
            tags = request.POST.getlist('tag')
            for tag in tags:
                t = Project_tag.objects.create(project=project,tag=tag)
                t.save()

        return redirect('/')

def show_project(request,pk):
    id = request.user.id
    usr = User.objects.get(id=id)
    project = Project.objects.get(pk=pk)
    usr2 = User.objects.get(username=project.author_id)
    try:
        check_following = UserFollowing.objects.get(user_id = usr,following_user_id=usr2)
        following = 'true'
    except:
        following = 'false'

    try:
        like = like_project.objects.get(user_id=usr , project=project)
        liked = 'true'
                    
    except:
        liked = 'false'
    
    notifications,count = get_notifications(id)
    return render(request,'project.html',{'project':project,'following':following,'liked':liked,'notifications':notifications,'count':count})


def collab_request(request,pk):
    id = request.user.id
    project = Project.objects.get(pk=pk)
    user = project.author_id
    usr = User.objects.get(id=id)
    col = collab.objects.create(project_id = project,requesting_user = usr,requested_user = user)
    col.save()
    
    # push notification
    mssg = f"{usr.username} just sent you a collab request"
    notify = notification.objects.create(user_id = user,notification_from=usr, notification_message = mssg)
    notify.save()   

    return HttpResponse("done")

def collabs(request):
    id = request.user.id
    usr = User.objects.get(id=id)

    try :
        data = request.GET['retrieve']
        if data == 'sent':
            col = collab.objects.filter(requesting_user= usr)
            
        if data == 'received':
            col = collab.objects.filter(requested_user = usr)
        
        data={}
        for x in col:
            data['project_title'] = x.project_id.title
            data['requesting_user'] = x.requesting_user.username
            data['requested_user'] = x.requested_user.username

            if data == 'received':
                url = usr.profile.pic.url
            else:
                user = User.objects.get(username = x.requested_user)
                url = user.profile.pic.url
            
            data['profile-url'] = url
        
        x = json.dumps(data)
        return HttpResponse(x)
    except:
        notifications,count = get_notifications(id)
        col = collab.objects.filter(requested_user=usr)
        return render(request,'collabs.html',{'collabs':col,'notifications':notifications,'count':count})