from django import forms
from . import models
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class AddAlbums(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"id":"required"}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"id":"required"}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    