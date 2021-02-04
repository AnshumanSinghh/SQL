from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request): 
    if not request.user.is_authenticated: # if user is not authenticated.
        return HttpResponseRedirect(reverse("login"))
    
    return render(request, "users/user.html")


def login_view(request):  
    if request.method == "POST":
        username = request.POST["username"] # get the username
        password = request.POST["password"] # get the password
        user = authenticate(request, username=username, password=password) # if the pass and uname match then give me who the user is.
        
        if user is not None: # means user authentication is successfull
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # if users fails to authenticate
            return render(request, "users/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")



def logout_view(request):  
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })

