from django.shortcuts import render
from .forms import registerForm 
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def Home(request):
    return render(request,'home.html')

def registered(request):

    form = registerForm()
    return render(request,'registration.html',{"form":form})

def logIn(request):
    form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

    