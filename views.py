from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate


# Create your views here
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return redirect("/")

def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user = authenticate(username="Sakshi",password='1234')
        if user is not None:
            return redirect("/")
        else:
            return redirect("/login")
    return render(request,'login.html')

def logoutuser(request):
    logout()
    return render(request,'/login')
