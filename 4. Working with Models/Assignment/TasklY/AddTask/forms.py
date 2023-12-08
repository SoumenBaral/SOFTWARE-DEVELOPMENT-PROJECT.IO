from . import models
from django import forms

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = models.TaskModel
        fields = '__all__'
        widgets = {
            'AssignDate': forms.DateInput(attrs={'type': 'date'}),
            'taskDescription':forms.Textarea(attrs={'class': 'custom-class', 'rows': 4, 'placeholder': 'Enter text here'})
            
        }
