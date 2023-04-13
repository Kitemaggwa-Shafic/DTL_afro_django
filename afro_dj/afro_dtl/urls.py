from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('about', views.about_us, name='about'),
    path('registration', views.registration, name='registration'),
]
