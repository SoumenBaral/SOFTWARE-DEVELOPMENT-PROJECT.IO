from django.shortcuts import render,redirect
from .forms import registerForm ,ChangeUserData
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm ,SetPasswordForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
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


@login_required  
def updateUser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                messages.success(request,"Update Profile  Successfully")
                return redirect("profile")
        else:
            form = ChangeUserData(instance=request.user)
            return render(request,'update.html',{'form':form})
    else:
        return redirect('register')


@login_required  
def changePassWithOld(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request," PassWord Change With old Password  Successfully Changed")
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passChange.html', {'form': form})
    else:
        return redirect('login')
    
@login_required  
def changePassWithOutOldPass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request," Change PassWord  Without  old Password  Successfully Changed")
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passChange.html', {'form': form})
    else:
        return redirect('login')

def Logout(request):
    logout(request)
    messages.warning(request,"Logged Out Successfully")
    return redirect('login')

    