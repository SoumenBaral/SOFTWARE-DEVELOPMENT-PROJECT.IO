from django.shortcuts import render
from . import forms
def AddAlbum(request):
    form = forms.AddAlbum 
    return render(request,'album.html',{"form":form})
