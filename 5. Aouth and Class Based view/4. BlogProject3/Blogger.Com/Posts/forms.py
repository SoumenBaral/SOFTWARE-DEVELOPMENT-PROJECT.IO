from django import forms
from . import models

class AddPost(forms.ModelForm):
    class Meta:
        model = models.Posts
        # fields = '__all__'
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['name', 'email', 'body']
