from django import forms
from django.contrib.auth.forms import AuthenticationForm

#creo un formulario de autenticacion personalizado
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', max_length=150)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

#creo un formulario de registro personalizado
class CustomUserCreationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    is_admin = forms.BooleanField(label='Es administrador', required=False)
    

