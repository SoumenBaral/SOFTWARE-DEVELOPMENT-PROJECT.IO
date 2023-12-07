from django.shortcuts import render
from .forms import AuthorForm

def AddAuthor(request):
    form = AuthorForm
    return render(request,'Author.html',{"form":form})
