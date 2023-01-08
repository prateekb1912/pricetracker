from django import forms
from django.forms import ModelForm

from .models import CustomUser

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['email', 'password']