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
