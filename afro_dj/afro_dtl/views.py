from django.shortcuts import render, redirect

# Using django contrib package and use the different methods in like authenticate, login, logout 
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import User_Signup

# Create your views here.

# My index view

# Showing how to use a variable in DTL and render this variable on HTML template
 
def index(request):
     # initiating a variable to use
    p_title = 'Afro Django Templating'
    # rendering a template and diaplsy it with whate ever is to be passed on with a request
    # we are sending a dic p_title a key and value p_title
    username = "Profic"
    gender = 'Male'
    return render(
        request,
        'index.html',
        {'p_title': p_title, 'username': username, 'gender': gender}
    ) 
 


# My default home page
def home(request):
    # return take on arguments, (request, 'page to return', display you need to render with this template)
    return render(request, 'home.html' )


# Preparing for the get request of the form
def register(request):
    return render(request, 'register.html' )


# About HTML 
def about_us(request):
    return render(request, 'about.html')


# user_sign up method to handle the user_signup 
def registration(request):
    # checking is the request is post
        user_name = request.POST['username']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        # created a simple user details list
        user_details = [user_name,email,gender,password]
        print(user_details)
        # return render(request, 'index.html', {'username':username, 'email':email})

        if User.objects.filter(username=user_name).first():
            print('Username already exists.')
            return render(request, 'login.html')
        else:
            user=User.objects.create_user(user_name,email,password)
            return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

def index_old(request):
    return render(request, 'index_old.html')


# Function to login in user
def login_user(request):
    user_name = request.POST['username']
    pwd = request.POST['password']
    # Check through username and see if the user_name posted here is = to what he has pu on form
    if User.objects.filter(username=user_name): 
        print("This username exists.")
        # sending authetic request to db for both username and password
        logged_user = authenticate(request, username=user_name, password=pwd)
        if logged_user is not None:
            # here we are logging in the user
            auth_login(request, logged_user)
            print(user_name+" "+"Logged in successfuly")
            return render( request, 'home.html', {'username': user_name, 'password': pwd} )
            # return redirect('home')
        else: 
            # Handling failed authentication of the user
            return render(request, 'login.html')
    else:
        print("User Credentials do not exist.")
        return render(request, 'login.html')
    

def login_page(request):
    return render(request, 'login.html')


@login_required
def logout_user(request):
    auth_logout(request)
    return redirect('login_page')