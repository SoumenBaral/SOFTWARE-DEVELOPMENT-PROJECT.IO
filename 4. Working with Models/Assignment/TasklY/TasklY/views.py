from django.shortcuts import render

def Home(request):
    return render(request,'Home.html')

def ShowTask(request):
    return render(request,'ShowTask.html')