from django.shortcuts import render,redirect
from . import forms
from . import models
from django.views.generic import CreateView ,UpdateView,DeleteView,DetailView
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
    success_url = reverse_lazy('profile')
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




class DetailsPost(DetailView):
    model = models.Posts
    pk_url_kwarg = 'id'
    template_name = 'postDetails.html'
    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post 
            new_comment.save()
        return self.get(request, *args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        
