
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label = 'UserName',label_suffix = '',widget = forms.TextInput(attrs={'placeholder':'Enter your UserName', 'class': 'form-control'}))
    password1 = forms.CharField(label = 'Password',label_suffix = '',widget = forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter your Password'}))
    password2 = forms.CharField(label = 'ConfirmPassword',label_suffix = '',widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Retype your Password'}))


    class Meta:
        model = User
        fields = ('username', 'email','password1','password2')
        widgets = {

            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Enter your Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Retype your Password'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(label = 'UserName',label_suffix='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your UserName '}))
    password = forms.CharField(label = 'Password',label_suffix = '',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the Password'}))