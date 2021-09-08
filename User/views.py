from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def user_profile(request, username):
    return render(request,'profile.html')

@login_required
def edit_profile(request, username):
    return render(request, 'edit-profile.html')
    