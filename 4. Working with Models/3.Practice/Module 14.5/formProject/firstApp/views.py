from django.shortcuts import render
from . forms import MyContact,MyModelForm
from .models import MyModel

def DjangoForm(request):
    form = MyContact(request.POST)
    return render(request,'djangoForms.html',{"form":form})

def DjangoModel(request):
    form = MyModelForm(request.POST)
    return render(request,"modleFrom.html",{"form":form})