from .models import Brand
from django import forms

class Brands(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['Name']