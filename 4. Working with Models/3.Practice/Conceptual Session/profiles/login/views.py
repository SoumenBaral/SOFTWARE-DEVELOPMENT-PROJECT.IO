from django.shortcuts import render,redirect
from django.http import HttpResponse
from .Dfrom import contactForm

# Create your views here.
def Home(request):
    # return HttpResponse("<h1 style='text-align:center;'>ami to vala na </h1>")
   
    return render(request,'home.html')

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        Email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,"home.html",{'name' : name, 'email': Email, 'select' : select})
    
    return render(request,'login.html')


def djangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        
    return render(request,'djangoform.html',{"form":form})