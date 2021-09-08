from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/explore')
    else:
        return render(request,'home.html')
    

def explore(request):
    return render(request,'explore.html')
    
 
def profile(request , username = "nitish"):
    return render(request,'profile.html')

def edit_profile(request):
    return render(request, 'edit-profile.html')