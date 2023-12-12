from django.shortcuts import render,redirect
from . import  forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout


# def AddAuthor(request):
#     if request.method == 'POST':
#         form =forms.AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('addAuthor')
        
#     else:
#         form = forms.AuthorForm
#         return render(request,'Author.html',{"form":form})
    

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
                return redirect('home')
            
            else:
                messages.warning(request,"No user Found")
                return redirect('register')
    else:
       form = AuthenticationForm
    return render(request,'register.html',{"form":form,'type' : 'Login'})
            
    

def userLogOut(request):
    logout(request)
    return redirect('login')

