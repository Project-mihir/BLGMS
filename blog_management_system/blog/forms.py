# blog/forms.py

from django import forms  # Import Django's forms module
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth.forms import UserCreationForm  # Import the built-in form

# Define the form class
class UserRegisterForm(UserCreationForm):
    # Add an email field to the form
    email = forms.EmailField(required=True)

    # Meta class to specify the model and fields
    class Meta:
        model = User  # Use Django's built-in User model
        fields = ['username', 'email', 'password1', 'password2']  # Fields to include in the form
