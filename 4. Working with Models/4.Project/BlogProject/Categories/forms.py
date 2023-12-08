from .models import Category
from django import forms

class AddCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'