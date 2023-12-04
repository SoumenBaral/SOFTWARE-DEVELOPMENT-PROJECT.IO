from django import forms
from firstApp.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name' : 'Student Name',
            'roll' : "Student Roll"
        }
        widgets  = {
            'name' : forms.TextInput(),
        }
        help_texts = {
            'name' : "Write your full name"
        }
        
        error_messages = {
            'name' : {'required' : 'Your name is required'}
        }
