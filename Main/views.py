from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Profile

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'explore.html')
    else:
        return render(request,'home.html')

def explore(request):
    return render(request,'explore.html')

def search(request):
    if request.GET.get('search'):
        keyword = request.GET['search']
        user =User.objects.all()
        found_users = []
        for i in user:
            if keyword == i.username or i.first_name == keyword:
                found_users.append(i)
                print(found_users)
        return render(request , "search_results.html" , {'users':found_users})

        
 
