from django.shortcuts import render,redirect
from . import  forms

def AddAuthor(request):
    if request.method == 'POST':
        form =forms.AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAuthor')
        
    else:
        form = forms.AuthorForm
        return render(request,'Author.html',{"form":form})

def AddProfiles(request):
    return render(request,'profiles.html')