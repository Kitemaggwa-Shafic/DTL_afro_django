from django.db import models

# Create your models here.

#  Creating a custom user model for signup
class User_Signup(models.Model):
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    signupdate = models.DateField(auto_now=True)

    def __str__(self):
        return self.username
# After this class, then create a view



#test model
class User_form_model(models.Model):
    name =  models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    occupation = models.CharField(max_length=1000)
    message = models.TextField(max_length=1000)
    def __str__(self):
        return self.name