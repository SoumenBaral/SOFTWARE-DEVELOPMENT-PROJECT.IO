from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def AddCat(request):
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AddCat')
    else:   
        form = forms.CategoryForm
        return render(request,'AddCat.html',{"form":form})