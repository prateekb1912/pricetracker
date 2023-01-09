from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

from .models import CustomUser

class UserForm(ModelForm):
    # password = forms.CharField(widget=PasswordInput)
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',  'email', 'password']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'labelData firstNameInput',
                'placeholder': 'steven'
            }),
            'last_name': TextInput(attrs={
                'class': 'labelData lastNameInput',
                'placeholder': 'smith'
            }),
            'email': EmailInput(attrs={
                'class': 'labelData emailNameInput',
                'placeholder': 'smudge@ca.au'
            }),
            'password': PasswordInput(attrs={
                'class': 'labelData',
                'placeholder': 'password'
            })
        }