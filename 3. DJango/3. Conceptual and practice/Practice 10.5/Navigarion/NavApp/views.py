from django.shortcuts import render

def NavHome(request):
    return render(request,"NavHome.html")

def contact(request):
    return render(request,"Contact.html")

def about(request):
    return render(request,"About.html")