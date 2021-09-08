from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

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
        user.save()
        auth_login(request , user)
        username = request.user.username
        return redirect('/user/{}'.format(username))
    else:
        return HttpResponse("get done")

def Logout(request):
    logout(request)
    return redirect('/')