from django import forms
from django.db import models
from .models import Comment, Services

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'authorEmail']
        

class ServicesForm(forms.ModelForm):
    
    class Meta:
        model = Services
        fields = ("name", 'email', 'order_type', 'DueDate',)

    
