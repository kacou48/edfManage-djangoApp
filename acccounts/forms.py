from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile, User


class UserRegistrationForm(UserCreationForm):
    accepter = forms.BooleanField(required = True)
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'accepter',
        ]

class LoginForm(forms.Form):
    email = forms.EmailField(label="")  
    password = forms.CharField(label="", widget=forms.PasswordInput) 


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = '__all__'
        exclude = ('user', 'status',)