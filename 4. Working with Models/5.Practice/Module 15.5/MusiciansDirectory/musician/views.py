from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def AddMusician(request):
    if request.method == 'POST':
        form = forms.AddMusician(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addMus')
    else:   
        form = forms.AddMusician
        return render(request,'musician.html',{"form":form})