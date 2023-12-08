from . import models
from django import forms

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = models.AddCategory
        fields = '__all__'