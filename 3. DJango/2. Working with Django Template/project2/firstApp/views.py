from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse('hello world you are my only world I do not have any ')
    return render(request, "firstApp/home.html")
