from django.shortcuts import render, redirect

# Using django contrib package and use the different methods in like authenticate, login, logout 
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import User_Signup, User_form_model

from .forms import User_form, Student_Form

from django. contrib import messages
import time

# Create your views here.

# My index view

# Showing how to use a variable in DTL and render this variable on HTML template
 
def index(request):
     # initiating a variable to use
    pr_title = 'Afro Django Templating'
    # rendering a template and diaplsy it with whate ever is to be passed on with a request
    # we are sending a dic pr_title a key and value pr_title
    if request.user.is_authenticated:
        username = request.user.username
        return render( request, 'index.html', {'pr_title': pr_title, 'username': username}  ) 
    else:
        author = 'Profic'
        gender = 'Male'
        return render( request, 'index.html', {'pr_title': pr_title, 'username': author, 'gender': gender} ) 

 

@login_required
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
            messages.error(request, 'Username already taken.')
            # print('Username already exists.')
            time.sleep(5)  # Delay for 5 seconds
            return render(request, 'login.html')
        else:
            user = User.objects.create_user(user_name,email,password)
            # Adding Success msgs with in the code block
            messages.success(request, 'The Student has been created successfully.')
            time.sleep(5)  # Delay for 5 seconds
            # Remove the message 
            
            # Saving my user details to my custome User_Signup model with save() function
            # user=User_Signup(username=user_name,email=email,gender=gender,password=password)
            # user.save()
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
            # Here we are logging in the user
            auth_login(request, logged_user)
            print(user_name+" "+"Logged in successfuly")
            # 
            messages.success(request, 'Successfuly logged in now!')
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


#  My logout user view
@login_required
def logout_user(request):
    auth_logout(request)
    # Adding messages
    messages.error(request, 'Successfuly loged out now!')
    return redirect('login_page')


# This view is for form of user to register and they get success msgs upon submission
def user_form(request):    
    form = User_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save() 
            messages.success(request, ("Your message has been sent successfully."))  
            #always remember to redirect to a view that handles the page and not the page
            return redirect('userforminfo.html')
        else:
            messages.success(request, "Your message not sent, Try again!!.")
            return redirect('user_form')   
    else:
        return render(request, 'userform.html', {'form':form})
    
def userforminfo(request):
    all_users = User_form_model.objects.all()
    return render(request, 'userforminfo.html', {'all':all_users})


#  Capture message view of the user
def cpature_message(request):
    messanger_field = request.POST['messanger']
    message_field = request.POST['message']
    captured_message = ChatBoX(messanger=messanger_field,  message=message_field)
    captured_message.save()
    chats =  ChatBox.objects.all()
    return render(request, 'chatbox.html', {'chats':chats})



def register_student(request):
    form = Student_Form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "New Student Saved Successfully !!")
            return redirect('userforminfo.html')
            # return redirect('registered_students.html')
        else:
            messages.error(request, "Student details not saved successfulyy, Try again !!")
            return render(request, 'register_student.html')
    else:
        return render(request, 'register_student.html')