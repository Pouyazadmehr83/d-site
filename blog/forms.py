from django import forms
from blog.models import Comment
from captcha.fields import CaptchaField




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'messages']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'messages': forms.Textarea(attrs={'class': 'form-control mb-10', 'rows': 5, 'placeholder': 'Message'}),
        }
