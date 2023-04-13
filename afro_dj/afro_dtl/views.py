from django.shortcuts import render

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


# About us HTML 
def about_us(request):
    return render(request, 'about.html')


# 
def user_signup(request):
    # checking is the request is post
    if request == "POST":
        username = request.POST.get['username'],
        email = request.POST.get['email'],
        gender = request.POST.get['gender'],
        password = request.POST.get['password'],
        cpassword = request.POST.get['cpassword'],
    else:
        pass