from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("This is your course")

def about(request):
    return HttpResponse("Do you know yourself..check your about")

def home(request):
    return HttpResponse("This is your first App")