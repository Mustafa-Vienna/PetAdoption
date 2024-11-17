from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, MinLengthValidator

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
