from django import forms
from django.forms.widgets import NumberInput

class MyContact(forms.Form):
    Name = forms.CharField()
    Comment = forms.CharField(widget=forms.Textarea)
    LittleComment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Email = forms.EmailField()
    Agree = forms.BooleanField()
    Date = forms.DateField()
    BirthDay = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    BirthYear = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    message = forms.CharField(max_length = 10,)
    first_name = forms.CharField(initial='Your name')