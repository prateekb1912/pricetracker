from django import forms
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import CustomUser

class UserCreationForm(ModelForm):
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

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
            return user

class UserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')
