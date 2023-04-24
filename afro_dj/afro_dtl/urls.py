from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index_old', views.index_old, name='index_old'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('about', views.about_us, name='about'),
    path('registration', views.registration, name='registration'),
    # friday session
    path('home/', views.login_user, name='login_user'), # receiving form data posted on the form and doing the login
    path('login_page', views.login_page, name='login_page'), # Handles login redirect
    path('logout_user', views.logout_user, name='logout_user'),
]
