from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
import re

#HOME PAGE
#IF USER SESSION, THEY CAN USE SITE FULLY
def index(request):
    return render(request, 'app_1/index.html')

#SIGNUP PAGE
def signup(request):
    return render(request, 'app_1/signup.html')

#VALIDATIONS AND REGISTRATION
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_password)
        request.session['user'] = new_user.id
        return redirect('/')
    return render(request, 'app_1/signup.html')

#LOGIN PAGE
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        l_email = User.objects.get(email=request.POST['email'])
        l_password = request.POST['password']
        passwords_match = bcrypt.checkpw(
            l_password.encode(), l_email.password.encode())
        if passwords_match:
            request.session['user'] = l_email.id
            return redirect('/success')
        else:
            return redirect('/')
    return render(request, 'app_1/login.html')

#OCEAN ADVENTURES LIST PAGE
def ocean_adventures(request):
    return render(request, 'app_1/view_ocean.html')

#MOUNTAIN ADVENTURES LIST PAGE
def mountain_adventures(request):
    return render(request, 'app_1/view_mountain.html')

#DESERT ADVENTURES LIST PAGE
def desert_adventures(request):
    return render(request, 'app_1/view_mountain.html')


