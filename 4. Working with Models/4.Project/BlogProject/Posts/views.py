from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def AddPost(request):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addPost')
    else:
        form = forms.AddPost
        return  render(request,'Posts.html',{"form":form})
    
def EditPost(request):
    pass