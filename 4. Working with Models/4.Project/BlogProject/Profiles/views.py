from django.shortcuts import render,redirect
from . import  forms

def AddProfiles(request):
    if request.method == 'POST':
        form =forms.ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addProf')
        
    else:
        form = forms.ProfileForm
        return render(request,'profiles.html',{"form":form})

