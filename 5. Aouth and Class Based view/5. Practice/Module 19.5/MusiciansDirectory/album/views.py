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
from django.views.generic import CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator


@method_decorator(login_required, name= 'dispatch')    
class AddAlbum(CreateView):
    model = models.Album
    form_class = forms.AddAlbums
    template_name = 'album.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully Added a Album')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request,"can't not create This Album")
        return response
    

    
@method_decorator(login_required, name= 'dispatch')
class EditPostView(UpdateView):
    model = models.Album
    form_class = forms.AddAlbums
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    def get_success_url(self):
        messages.success(self.request,'Update done ')
        return reverse_lazy('home')
    

@method_decorator(login_required, name= 'dispatch')
class DeletePostView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    def get_success_url(self):
        messages.success(self.request,'Delete done ')
        return reverse_lazy('home')

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
    

@method_decorator(login_required, name= 'dispatch')
class UserLogoutViewClass(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
       return reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        messages.success(self.request, "You have been successfully logged out.")
        return response