from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from Main.models import Profile

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            auth_login(request , user)
            return redirect('/')
        else:
            return HttpResponse("wrong credentials")
    else:
        return render(request, 'login.html')
def sign_up(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(first_name = firstname , username = username , email = email , password = password)
        # profile = Profile.objects.create(user = user)
        # profile.save()
        user.save()
        auth_login(request , user)
        username = request.user.username
        return redirect('/welcome')
        # return redirect('/user_{}'.format(username))
    else:
        return HttpResponse("get done")

def update(request):
        id = request.user.id
        user = User.objects.get(pk=id)
        username = request.POST['username']
        bio = request.POST['About']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if 'image' in request.FILES:
            image = request.FILES['image']
            user.profile.pic = image
        user.username = username
        user.first_name = firstname
        user.last_name = lastname
        user.profile.about = bio
        user.save()
        return redirect('/')

def Logout(request):
    logout(request)
    return redirect('/')


