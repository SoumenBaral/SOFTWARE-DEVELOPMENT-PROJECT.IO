from django import forms
from . import models

class AddCarForm(forms.ModelForm):
    class Meta:
        model = models.AddCar
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']