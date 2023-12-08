from django.shortcuts import render
from . import forms

# Create your views here.
def AddMusician(request):
    form = forms.AddMusician
    return render(request,'musician.html',{"form":form})