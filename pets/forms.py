from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Leave your Comment"
        }
        widgets = {
            "user_name": forms.TextInput(attrs={'class': 'form-control mb-3'}),
            "user_email": forms.EmailInput(attrs={'class': 'form-control mb-3'}),
            "text": forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 5}),
        }


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'pet_name', 'pet_age', 'excerpt', 'image', 'content'
        ]
