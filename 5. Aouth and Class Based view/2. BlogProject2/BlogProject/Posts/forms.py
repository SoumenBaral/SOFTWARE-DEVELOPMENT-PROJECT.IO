from django import forms
from . import models

class AddPost(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields = '__all__'
