from django.shortcuts import render
from . forms import MyContact

def DjangoForm(request):
    form = MyContact(request.POST)
    return render(request,'djangoForms.html',{"form":form})
