from django import forms
from .models import FileModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        # labels = {'username':"Username", 'email':"Email", 'password1': 'Password', "password2":"Confirm Password"}
    username = forms.CharField(label="Username",widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
    email = forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))
    password2 = forms.CharField( label="Confirm Password",widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}))



class MultipleFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = '__all__'

        widgets = {
            "files": forms.FileInput(attrs={'multiple': True, 'class':'form-control'}),
            "name": forms.TextInput(attrs={'class':'form-control'}),

        }
