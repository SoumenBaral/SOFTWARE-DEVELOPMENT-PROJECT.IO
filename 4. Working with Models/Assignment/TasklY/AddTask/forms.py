from . import models
from django import forms

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = models.TaskModel
        fields = '__all__'
        widgets = {
            'AssignDate': forms.DateInput(attrs={'type': 'date'})
        }
