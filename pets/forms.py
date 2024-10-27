from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "author", "email"]
        labels = {
            "text": "Leave your Comment"
        }
        widgets = {
            "text": forms.Textarea(attrs={'class': 'form-control mb-3', 'rows': 5}),
        }


class UserPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'pet_name', 'pet_age', 'excerpt', 'image', 'content'
        ]
