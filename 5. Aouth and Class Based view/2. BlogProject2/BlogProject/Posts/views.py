from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def AddPost(request):
    if request.method == 'POST':
        form = forms.AddPost(request.POST)
        if form.is_valid():
            # form.cleaned_data['author'] = request.user
            form.instance.author = request.user
            form.save()
            return redirect('addPost')
    else:
        form = forms.AddPost
        return  render(request,'Posts.html',{"form":form})
    
def EditPost(request,id):
    post = models.Posts.objects.get(pk=id)
    print(post.Name)
    if request.method == 'POST':
        form = forms.AddPost(request.POST ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AddPost(instance=post)
        return  render(request,'Posts.html',{"form":form})

def DeletePost(request,id):
    post = models.Posts.objects.get(pk=id)
    post.delete()
    return redirect('home')