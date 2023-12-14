from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class registerForm(UserCreationForm):
    FirstName = forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    LastName = forms.CharField(widget=forms.TextInput(attrs={'id': 'required'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ("username","FirstName","LastName","email")


   