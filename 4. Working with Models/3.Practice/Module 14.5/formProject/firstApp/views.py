from django.shortcuts import render
from . forms import MyContact
from .models import MyModel

def DjangoForm(request):
    form = MyContact(request.POST)
    return render(request,'djangoForms.html',{"form":form})

def DjangoModel(request):
    form =  MyModel
    return render(request,"modleFrom.html",{"form":form})