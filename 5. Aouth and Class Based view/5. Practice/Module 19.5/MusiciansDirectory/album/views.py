from django.shortcuts import render,redirect
from . import forms
from . import models
def AddAlbum(request):
    if request.method == 'POST':
        form = forms.AddAlbums(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAlbum')
    else:   
        form = forms.AddAlbums 
        return render(request,'album.html',{"form":form})

def EditAlbum(request,id):
    post = models.Album.objects.get(pk=id)
   
    if request.method == 'POST':
        form = forms.AddAlbums(request.POST ,instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AddAlbums(instance=post)
        return  render(request,'album.html',{"form":form})
    
def DeletePost(request,id):
    post = models.Album.objects.get(pk=id)
    post.delete()
    return redirect('home')