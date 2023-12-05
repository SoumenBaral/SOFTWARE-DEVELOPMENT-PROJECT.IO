from django import forms


class MyContact(forms.Form):
    Name = forms.CharField()
    Comment = forms.CharField(widget=forms.Textarea)