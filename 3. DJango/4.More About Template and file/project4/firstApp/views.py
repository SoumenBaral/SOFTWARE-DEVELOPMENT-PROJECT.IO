from django.shortcuts import render

def AppHome(request):
    return render(request,'index.html')
