from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

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


class RegistrationForms(CreateView):
    template_name = 'registration.html'
    form_class = forms.RegistrationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Successfully Create an Account Now LogIN ')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request, 'SignUp in information incorrect')
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context
    
    
    


class UserLoginView(LoginView):
    template_name ='registration.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    
    
    def form_invalid(self, form: AuthenticationForm) -> HttpResponse:
        messages.warning(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    

def logOut(request):
    logout(request)
    messages.success(request,'done')
    return redirect('home')