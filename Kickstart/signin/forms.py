from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        # widgets = {
        #     'username':forms.TextInput(attrs={'placeholder':'Username'}),
        #     'email':forms.EmailInput(attrs={'placeholder':'Email'}),
        #     'password1':forms.PasswordInput(attrs={'placeholder':'password1'}),
        #     'password2':forms.PasswordInput(attrs={'placeholder':'password2'}),
        # }
        fields =['username', 'email', 'password1', 'password2']
