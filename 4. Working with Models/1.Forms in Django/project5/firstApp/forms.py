from django import forms

class contactForm(forms.Form):
    Name = forms.CharField(label='Name')
    Email = forms.EmailField(label='Email')
    Age = forms.IntegerField()
    Weight = forms.FloatField()
    Balance = forms.DecimalField()
    checked = forms.BooleanField()
    Birthday = forms.DateField()
    Appointment =forms.DateTimeField() 
    CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    Size = forms.ChoiceField(choices=CHOICES)

    pizza = forms.MultipleChoiceField(choices=CHOICES)
