from django.shortcuts import render


def navHome(request):
    return render(request,"navHome.html"),

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"ContactUs.html")

def blog(request):
    return render(request , "Bolog.html")