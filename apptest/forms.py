from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User


class UsuarioForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':"username", 'class':"form-control", 'id':"username" , 'placeholder': "Nombre de Usuario", 'name':"username"}))
    email= forms.EmailField(widget=forms.TextInput(attrs={'type':"email", 'class':"form-control", 'id':"email" , 'placeholder': "Correo Electrónico", 'name':"email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password", 'class':"form-control", 'id':"password" , 'placeholder': "Contraseña", 'name':"password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password", 'class':"form-control", 'id':"password" , 'placeholder': "Contraseña", 'name':"password"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos del formulario, le asigna un valor vacio