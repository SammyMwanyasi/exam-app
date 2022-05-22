from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    date_of_birth = forms.DateTimeField(help_text='Date Of Birth')

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth',
                  'password1', 'password2']