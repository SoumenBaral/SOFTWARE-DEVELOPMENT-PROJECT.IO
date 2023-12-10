from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.
def Home(request):
    return render(request,'home.html')

def signUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save(commit=False)
            print(form.cleaned_data)
        
        else :
            form = RegistrationForm()
            return render(request,'signUp.html',{"form":form})

