from django.shortcuts import render,redirect
from . import forms
from django.views.generic import CreateView
from . import models
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
# def AddMusician(request):
#     if request.method == 'POST':
#         form = forms.AddMusician(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('addMus')
#     else:   
#         form = forms.AddMusician
#         return render(request,'musician.html',{"form":form})
    

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
    