from django import forms
from . import models

class AddAlbums(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'