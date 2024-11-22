from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    A form for submitting comments on posts

    Excludes the post, author, and email fields
    as these are automatically populated
    """
    class Meta:
        model = Comment
        exclude = ["post", "author", "email"]
        labels = {
            "text": "Leave your Comment"
        }
        widgets = {
            "text": forms.Textarea(attrs={
                'class': 'form-control mb-3', 'rows': 5}),
        }


class UserPostForm(forms.ModelForm):
    """
    A form for creating or updating posts

    Including the following fields:
    title, pet name, pet age, excerpt, image, and content

    Adds a widget for pet age with a defined min and max values
    """
    class Meta:
        model = Post
        fields = [
            'title', 'pet_name', 'pet_age', 'excerpt', 'image', 'content'
        ]
        widgets = {
            'pet_age': forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }
