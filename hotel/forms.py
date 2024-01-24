from django import forms
from .models import Comment,ContactUs

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'ratings', 'body']
        
        
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']