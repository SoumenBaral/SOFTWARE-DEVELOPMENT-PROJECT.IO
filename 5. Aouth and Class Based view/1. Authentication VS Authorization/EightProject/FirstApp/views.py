from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.
def Home(request):
    return render(request,'home.html')

def signUp(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success("Account Created Successfully")
                form.save()
                print(form.cleaned_data)
            
        else :
            form = RegistrationForm()
        return render(request,'signUp.html',{"form":form})
    else:
        return redirect('home')

def user_login(request):
    pass

def profile(request):
    pass

def LogOut(request):
    pass

def PassChangeWithOldPass(request):
    pass
def PassChangeWithoutOldPass(request):
    pass

def changeUserData(request):
    pass