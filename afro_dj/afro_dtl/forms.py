from django import forms
from .models import User_form_model, Reg_Student


# The purpose of this class is to define a standardized way for users to submit information 
# based on the fields specified in the model. 
# This can be used to easily create forms for user input in a web application, 
# and to validate and process the data submitted by the user.
class User_form(forms.ModelForm):
    class Meta:
        model = User_form_model
        fields = ['name', 'email','occupation', 'message']

# Student form details
class Student_Form(forms.ModelForm):
    class Meta:
        model = Reg_Student
        fields =['firstname','lastname','stdClass','gender','age','address']