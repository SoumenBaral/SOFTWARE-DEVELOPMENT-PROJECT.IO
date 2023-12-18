from django.shortcuts import render
from . import forms
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView,UpdateView,DeleteView,View
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator
from carModel.models import BuyCar
# Create your views here.

class RegistrationForms(CreateView):
    template_name = 'register.html'
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
    template_name ='register.html'

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

class ProfileView(View):
    template_name = 'profile.html'
    def get(self, request, *agrs, **kwargs):
        data = BuyCar.objects.filter(user=request.user)
        return render(request, 'profile.html',{'data':data})

@method_decorator(login_required, name= 'dispatch')
class logOut(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
       messages.success(self.request, "You have been successfully logged out.")
       return reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response