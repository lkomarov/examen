from django import forms
from .models import Producto, Carrito, ItemCarrito
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        
class AgregarProductoForm(forms.Form):
    cantidad = forms.IntegerField(min_value=1, label='Cantidad', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]