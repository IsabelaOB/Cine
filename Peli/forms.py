# forms.py (dentro de tu aplicación)
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    # Agrega campos personalizados si es necesario
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomAuthenticationForm(AuthenticationForm):
    # Puedes personalizar este formulario si es necesario
    class Meta:
        model = User
