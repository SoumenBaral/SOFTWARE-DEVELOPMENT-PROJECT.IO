from django import forms

class contactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(label="Your Email")