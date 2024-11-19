from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, MinLengthValidator
from django.utils.html import format_html

name_validator = RegexValidator(
    r'^[a-zA-Z0-9]*$', 'Username can only contain letters and numbers.'
)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(
        validators=[
            MinLengthValidator(3, message="Username must be at least 3 characters long."),
            name_validator
        ],
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                format_html("This username already taken.<br>Please supply a different username!")
                )
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                format_html("This email is already in use.<br>Please supply a different email address!")
                )
        return email