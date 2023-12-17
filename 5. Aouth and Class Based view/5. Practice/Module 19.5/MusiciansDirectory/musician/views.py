from django.shortcuts import render,redirect
from . import forms
from django.views.generic import CreateView,UpdateView
from . import models
from django.contrib import messages
from django.urls import reverse_lazy
    

class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.AddMusician
    template_name = 'musician.html'
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully Added a Musicians')
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.warning(self.request,"can't not create and Musician")
        return response

class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.AddMusician
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    def get_success_url(self):
        messages.success(self.request,'Update done ')
        return reverse_lazy('home')
    