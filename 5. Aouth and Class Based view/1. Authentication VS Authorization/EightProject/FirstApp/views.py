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
                messages.success(request,"Account Created Successfully")
                form.save()
                print(form.cleaned_data)
                return redirect('home')
            
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
    logout(request)
    return redirect('signUp')

def PassChangeWithOldPass(request):
    pass
def PassChangeWithoutOldPass(request):
    pass

def changeUserData(request):
    pass