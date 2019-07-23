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
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],                                    birthday=request.POST['birthday'], email=request.POST['email'], password=hashed_password)
        request.session['user'] = new_user.id
        return redirect('/success')
    return render(request, 'app_1/signup.html')

#LOGIN PAGE
def login(request):
    return render(request, 'app_1/login.html')

