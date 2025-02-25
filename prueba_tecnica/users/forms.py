from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['name', 'last_name', 'email', 'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado.')
        return email
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('La contraseña debe contener al menos un número.')
        return password

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)