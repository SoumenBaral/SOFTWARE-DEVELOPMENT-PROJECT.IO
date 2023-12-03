from django import forms

class contactForm(forms.Form):
    Name = forms.CharField(label='Name')
    Email = forms.EmailField(label='Email')
