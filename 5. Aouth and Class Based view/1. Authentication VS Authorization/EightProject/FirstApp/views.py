from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.
def Home(request):
    return render(request,'home.html')

def signUp(request):
    pass
