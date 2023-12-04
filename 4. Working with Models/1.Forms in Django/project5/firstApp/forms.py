from django import forms

class contactForm(forms.Form):
    Name = forms.CharField( label="Full Name : ", help_text="Total length must be within 70 characters", required=False, error_messages={'required': 'Please enter your name.'},widget = forms.Textarea(attrs = {'id' : 'text_area', 'class' : 'class1 class 2', 'placeholder' : 'Enter your name'},))
    # Email = forms.EmailField(label='Email')
    # Age = forms.IntegerField()
    # Weight = forms.FloatField()
    # Balance = forms.DecimalField()
    # checked = forms.BooleanField()
    # Birthday = forms.DateField()
    # Appointment =forms.DateTimeField() 
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # Size = forms.ChoiceField(choices=CHOICES)

    # pizza = forms.MultipleChoiceField(choices=CHOICES)

    file = forms.FileField()




class StudentData(forms.Form):
    name =forms.CharField(widget=forms.TextInput)
    email =forms.CharField(widget=forms.EmailInput)

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname) < 10:
            raise forms.ValidationError("Enter a name with at least 10 characters")    
        if '.com' not in valemail:
            raise forms.ValidationError("Your email must Have to  contain .com")
