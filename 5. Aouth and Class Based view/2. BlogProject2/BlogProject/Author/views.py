from django.shortcuts import render,redirect
from . import  forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from Posts.models import Posts
    

def Register(request):
    if request.method == 'POST':
        form =forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'register in Successfully')
            return redirect('login')
    else:
       form = forms.RegistrationForm
    return render(request,'register.html',{"form":form,'type' : 'Register'})

def LogIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            userName = form.cleaned_data['username']
            passWord = form.cleaned_data['password']
            user = authenticate(username = userName,password = passWord )

            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            
            else:
                messages.warning(request,"No user Found")
                return redirect('register')
    else:
       form = AuthenticationForm
    return render(request,'register.html',{"form":form,'type' : 'Login'})
            
    

def userLogOut(request):
    logout(request)
    return redirect('login')

@login_required
def profile (request):
    data = Posts.objects.filter(author = request.user)
    return render(request,'profile.html',{'data': data})

@login_required
def EditProfile(request):
    if request.method == "POST":
        form = forms.ChangeUserForm(request.POST,instance = request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:   
        form = forms.ChangeUserForm(instance = request.user)
    return render(request,'updateUser.html',{'form':form})

@login_required
def changePassWithOldPass(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user , data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Successfully changed your Password')
            return redirect('profile')
    else:   
        form = PasswordChangeForm(user=request.user)
    return render(request,'passwordChange.html',{'form':form})