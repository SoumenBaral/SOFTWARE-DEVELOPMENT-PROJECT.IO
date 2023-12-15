from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView ,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

# Function Views....................................................
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
    

# Class View ...........................................................
    
class AddPostCreateView(CreateView):
    model = models.Posts
    form_class = forms.AddPost
    template_name = "Posts.html"
    success_url = '/author/profile/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
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


class UpdatePost(UpdateView):
    model = models.Posts
    form_class = forms.AddPost
    template_name = "Posts.html"
    pk_url_kwarg='id'
    success_url = reverse_lazy('profile')




def DeletePost(request,id):
    post = models.Posts.objects.get(pk=id)
    post.delete()
    return redirect('home')

class DeleteViewed(DeleteView):
        model = models.Posts
        template_name = "delete.html"
        pk_url_kwarg='id'
        success_url = reverse_lazy('profile')




