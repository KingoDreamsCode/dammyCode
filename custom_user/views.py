import os
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from .models import PDFFile
from custom_user.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .models import Blog


def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

def shop(request):
    return render(request, 'shop.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        print(request.POST)  
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        password2 = request.POST['password2']

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Invalid email format.")
            return redirect('signup')

        # Validate password length
        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            return redirect('signup')

        # Validate mixed characters in the password
        if not any(char.islower() for char in password) or not any(char.isupper() for char in password):
            messages.error(request, "Password must have both lowercase and uppercase characters.")
            return redirect('signup')

        try:
            validate_password(password, User(email=email))
        except ValidationError as e:
            error_messages = ', '.join(e.messages)
            messages.error(request, error_messages)
            return redirect('signup')

        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already used")
                return redirect('signup')
            
            user = User.objects.create_user(email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            
            messages.success(request, "Your account has been created successfully")
            return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('signup')
    
    return render(request, 'signup.html')

@login_required(login_url='login')
def pdf_list(request):
    categories = PDFFile.CATEGORY_CHOICES
    departments = PDFFile.DEPARTMENT_CHOICES
    years = PDFFile.objects.order_by('-year').values_list('year', flat=True).distinct()
    types = PDFFile.TYPE_CHOICES

    category = request.GET.get('category')
    department = request.GET.get('department')
    year = request.GET.get('year')
    type = request.GET.get('type')

    pdf_files = PDFFile.objects.all()

    if category:
        pdf_files = pdf_files.filter(category=category)
    if department:
        pdf_files = pdf_files.filter(department=department)
    if year:
        pdf_files = pdf_files.filter(year=year)
    if type:
        pdf_files = pdf_files.filter(type=type)

    context = {
        'pdf_files': pdf_files,
        'categories': categories,
        'departments': departments,
        'years': years,
        'types': types,
        'selected_category': category,
        'selected_department': department,
        'selected_year': year,
        'selected_type': type,
    }
    return render(request, 'shop.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')