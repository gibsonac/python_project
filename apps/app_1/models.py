from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
#REGISTRATION VALIDATOR
    def basic_validator(self, postData):
        errors = {}
        result = User.objects.filter(email=postData['email'])
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData["email"]) < 5:
            errors["email"] = "Email should be at least 5 characters"
        if len(result) > 0:
            errors['emails'] = "Email already exists, log in or use another email"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email_format"] = "Email should be in 'name@mail.com' format"
        if len(postData["password"]) < 6:
            errors["password"] = "Your password must be at least 6 characters. Please try another."
        if postData['password'] != postData['confirm_password']:
            errors['password_match'] = "Password does not match with confirm password."
        return errors

#LOGIN VALIDATOR
    def login_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Email must be in format "name@mail.com"'
        if not User.objects.filter(email=postData['email']):
            errors['emails'] = "Email address not recognized"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        return errors

#OCEAN ADVENTURES LIST PAGE
    def ocean_adventures (request):
        pass
        return render (request, 'app_1/view_ocean.html')
    
#MOUNTAIN ADVENTURES LIST PAGE
    def mountain_adventures (request):
        pass
        return render (request, 'app_1/view_mountain.html')

#DESERT ADVENTURES LIST PAGE
    def desert_adventures (request):
        pass
        return render (request, 'app_1/view_mountain.html')

#USER DATABASE
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	user_level = models.PositiveIntegerField(default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Location(models.Model):
	city = models.CharField(max_length=255)
	district = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Adventure(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	rating = models.PositiveIntegerField()
	likes = models.PositiveIntegerField()
	photos = models.ImageField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User, related_name="adventure_created")
	located = models.ForeignKey(Location, related_name="adventure_located")

class Message(models.Model):
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	creator = models.ForeignKey(User, related_name="message_created")
	adventure_posted = models.ForeignKey(Adventure, related_name="adventure_messages")
