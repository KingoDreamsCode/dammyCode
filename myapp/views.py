import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .models import PDFFile


def index(request):
    #obj = PDFFile.objects.all()
    return render(request, 'index.html')
def shop(request):
    #obj = PDFFile.objects.all()
    return render(request, 'shop.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        my_user = auth.authenticate(username = username, password = password)
        
        if my_user is not None:
            auth.login(request, my_user)
            return redirect('index')
        else:
            messages.info(request, 'Wrong Details')
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,"Email Already Used")
                return redirect('signup')
            else:
                my_user = User.objects.create_user(username = username, password = password)
                my_user.first_name = fname
                my_user.last_name = lname
                
                my_user.save()
                messages.success(request, "Your account has been created successfully")
                return redirect('login')
        
        else:
            messages.info(request,"Passwords do not correspond")
            return redirect('signup')

    return render(request, 'signup.html')