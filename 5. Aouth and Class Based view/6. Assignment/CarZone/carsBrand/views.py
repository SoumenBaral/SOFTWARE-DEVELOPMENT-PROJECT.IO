from django.shortcuts import render ,redirect
from . import forms
from django.contrib import messages

def AddBrand(request):
    if request.method == 'POST':
        form =forms.Brands(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Car Brand Added Successfully ')
            return redirect("addBread")
    else:
        Form = forms.Brands
        return render(request,'brand.html',{"Form":Form})