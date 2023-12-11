from django.shortcuts import render,redirect
from .forms import RegistrationForm ,ChangeUserData
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
                return redirect('login')
            
        else :
            form = RegistrationForm()
        return render(request,'signUp.html',{"form":form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                    name = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    user = authenticate(username=name,password=password)
                    login(request,user)
                    messages.warning(request,"LoggedIn Successfully ")
                    return redirect("home")
  
        else:
            form = AuthenticationForm()
            return render(request,"login.html",{'form':form})
    else: 
       return redirect("profile")


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                return redirect("profile")
        else:
            form = ChangeUserData(instance=request.user)
            return render(request,'profile.html',{'form':form})
    else:
        return redirect('signUp')

def LogOut(request):
    logout(request)
    return redirect('signUp')

def PassChangeWithOldPass(request):
    pass
def PassChangeWithoutOldPass(request):
    pass

def changeUserData(request):
    pass