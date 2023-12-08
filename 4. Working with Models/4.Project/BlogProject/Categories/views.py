from django.shortcuts import render ,redirect
from . import forms
# Create your views here.
def AddCategories(request):
    if request.method == 'POST':
        form =forms.AddCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addCat")
    else:
        Form = forms.AddCategory
        return render(request,'Categories.html',{"Form":Form})