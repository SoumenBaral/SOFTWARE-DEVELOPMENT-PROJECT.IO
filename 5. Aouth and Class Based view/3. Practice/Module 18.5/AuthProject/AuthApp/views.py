from django.shortcuts import render,redirect
from .forms import registerForm ,ChangeUserData
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def Home(request):
    return render(request,'home.html')

def registered(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created Successfully")
            print(form.cleaned_data)
            return  redirect("login")

    else:
        form = registerForm()
    return render(request,'registration.html',{"form":form})

def logIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=name,password=password)
            login(request,user)
            messages.success(request,"Logged In Successfully")
            print(form.cleaned_data)
            return  redirect("home")

    else:
        form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

@login_required   
def Profile(request):
    return render(request,'profile.html')

def updateUser(request):
    pass

def changePassWithOld(request):
    pass
def changePassWithOutOldPass(request):
    pass
def Logout(request):
    logout(request)
    messages.warning(request,"Logged Out Successfully")
    return redirect('login')

    