from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def clean_first_name(self):
        if self.cleaned_data["first_name"] == '':
            raise ValidationError("First name is required.")
        return self.cleaned_data["first_name"]
    
    def clean_last_name(self):
        if self.cleaned_data["last_name"] == '':
            raise ValidationError("Last name is required.")
        return self.cleaned_data["last_name"]
           
    def clean_email(self):
        if self.cleaned_data["email"] == '':
            raise ValidationError("Email is required.")
        return self.cleaned_data["email"]