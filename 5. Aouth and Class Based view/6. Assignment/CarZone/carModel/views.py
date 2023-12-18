from django.shortcuts import render
from . import models,forms
from django.views.generic import CreateView ,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name= 'dispatch') 
class AddPostCreateView(CreateView):
    model = models.AddCar
    form_class = forms.AddCarForm
    template_name = "addCar.html"
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully Added Car')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request,"can't not create Post For this Car ")
        return response