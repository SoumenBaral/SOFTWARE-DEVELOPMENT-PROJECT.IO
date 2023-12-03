from django.shortcuts import render
from .forms import contactForm

def About(request):
    if(request.method == "POST"):
        print(request.POST)
        name =request.POST.get("username")
        email =request.POST.get("email")
        select =request.POST.get("select")
        return render(request,'about.html',{"name":name,"email":email,'select':select})
    return render(request,'about.html')

def Form (request):       
    return render(request,'Form.html')


def DjangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'django_form.html',{"form":form})