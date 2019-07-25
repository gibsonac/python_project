from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Adventure, Location, Message
import bcrypt
import re



#HOME PAGE
#IF USER SESSION, THEY CAN USE SITE FULLY
def index(request):
    if 'user' in request.session:
        return redirect('/home')
    else:
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
        return redirect('/home')
    return render(request, 'app_1/signup.html')

#LOGIN PAGE
def login_page(request):
    return render(request, 'app_1/login.html')

#LOGIN PROCESS
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
            return redirect('/home')
        else:
            return redirect('/home')
    return render(request, 'app_1/login.html')

#HOME ONCE LOGGED IN
def home(request):
    if not 'user' in request.session:
        messages.error(request, "You must log in.")
        return redirect('/login_page')
    else:
        return render(request, 'app_1/home.html', {'user': User.objects.get(id=request.session['user'])})

#EDITING YOUR USER PROFILE
def user_edit (request):
    print(User.objects.get(id = request.session['user']))
    context = {
        "this_user": User.objects.get(id=request.session['user']),
    }
    return render (request, 'app_1/edit_user.html', context)

#SUBMITTING YOUR CHANGES TO USER PROFILE
def user_submit_edit (request, my_val):
    this_user = User.objects.get(id = request.session['user'])
    errors = User.objects.edit_user_validator(request.POST)
    if this_user.email == request.POST['email']:
        pass
    else:
        all_emails = User.objects.filter(email = request.POST['email'])
        if len(all_emails) >= 1:
            errors['email_already_used'] = "This email already exists!"
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect (f'/user/edit')
    else:
        if request.method == "POST":
            edit_user = User.objects.get(id = my_val)
            edit_user.first_name = request.POST['first_name']
            edit_user.last_name = request.POST['last_name']
            edit_user.email = request.POST['email']
            edit_user.description = request.POST['description']
            edit_user.save()
    return redirect('/home')

#OCEAN ADVENTURES LIST PAGE
def ocean_adventures(request):
    all_adventures = Adventure.objects.all()
    context = {
    "adventures": all_adventures.filter(category="ocean")
    }
    return render(request, 'app_1/view_ocean.html', context)

#MOUNTAIN ADVENTURES LIST PAGE
def mountain_adventures(request):
    all_adventures = Adventure.objects.all()
    context = {
    "adventures": all_adventures.filter(category="mountain")
    }
    return render(request, 'app_1/view_mountain.html', context)

#DESERT ADVENTURES LIST PAGE
def desert_adventures(request):
    all_adventures = Adventure.objects.all()
    context = {
    "adventures": all_adventures.filter(category="desert")
    }
    return render(request, 'app_1/view_desert.html', context)

#ADD AN ADVENTURE PAGE
def add_adventure(request):
    return render(request, 'app_1/add_adventure.html')

#ADD NEW ADVENTURE
def new_adventure(request):
    errors = Adventure.objects.adventure_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/add_adventure')
    else:
        creator = User.objects.get(id=request.session['user'])
        Location.objects.create(
            city = request.POST['city'], district = request.POST['district']
        )
        added_location = Location.objects.last()
        Adventure.objects.create(
            title=request.POST['title'], description = request.POST['description'], located=added_location, creator = creator, category=request.POST['category'])
        new_adventure = Adventure.objects.last()
        Message.objects.create(creator = creator, adventure_posted = new_adventure, rating = int(request.POST['rating']))
        return redirect('/home')

#ADVENTURE DETAILS
def adventure_details (request, my_val):
    adventure = Adventure.objects.get(id = my_val)
    all_ratings = adventure.adventure_ratings.all()
    avg_rating = 0
    if len(all_ratings) == 0:
        pass
    else:
        total = 0
        for rating in all_ratings:
            total = total + rating
        avg_rating = total/len(all_ratings)
    context = {
        "adventure": Adventure.objects.get(id = my_val),
        "avg_rating": avg_rating,
    }
    return render(request, 'app_1/adventure_details.html', context)

#LOGOUT
def logout(request):
    request.session.clear()
    return redirect('/')

