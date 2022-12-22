from django import forms


class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    nacionalidad = forms.CharField(max_length=50)
    fechaNacimiento = forms.DateField() 