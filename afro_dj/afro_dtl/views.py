from django.shortcuts import render

# Using django contrib package and use the different methods in like authenticate, login, logout 
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# My index view


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


# Preparing for the get request of the form
def register(request):
    # return take on arguments, (request, 'page to return', display you need to render with this template)
    return render(request, 'register.html' )


# About HTML 
def about_us(request):
    return render(request, 'about.html')


# user_sign up method to handle the user_signup 
def registration(request):
    # checking is the request is post
        username = request.POST['username']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']

        # created a simple user details list
        user_details = [username,email,gender,password]
        print(user_details)
        return render(request, 'index.html', {'username':username, 'email':email})
    