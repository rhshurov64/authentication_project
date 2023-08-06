from django import forms
from django.contrib.auth.forms import UserCreationForm, 
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
    password1 = forms.CharField(label= 'Password ', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label= 'Password Again', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(label= 'Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label= 'First name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label= 'Last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label= 'Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        lables = {
            'first_name' :'First Name',
            'last_name' :'Last Name',
            
        }



