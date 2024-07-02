from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Galon, Marca

class GalonesForms(forms.ModelForm):
    class Meta: 
        model=Galon
        fields=['idGalon', 'kg', 'marca', 'cantidad', 'imagen']
        labels={
            'idGalon': 'idGalon',
            'kg': 'kg',
            'marca': 'marca',
            'cantidad': 'cantidad',            
            'imagen': 'imagen'
        }
        widgets={
            'idGalon': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese Id del galon',
                    'id':'idGalon'
                }
            ),
            'kg': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese KG del galon',
                    'id':'kg'
                }
            ),
            'marca': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese marca del galon',
                    'id':'marca'
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese cantidad de galones',
                    'id':'cantidad'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id':'imagen'
                }
            )
            
            }






class PerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }




class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']