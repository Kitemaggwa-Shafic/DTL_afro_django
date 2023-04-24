from django.contrib import admin
from . models import User_Signup, Reg_Student, User_form_model

# Register your models here.

admin.site.register(User_Signup),
admin.site.register(User_form_model),
admin.site.register(Reg_Student),
