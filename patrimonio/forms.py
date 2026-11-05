from django import forms
from .models import LugarPatrimonial

class LugarPatrimonialForm(forms.ModelForm):
    class Meta:
        model = LugarPatrimonial
        fields = ['nombre', 'categoria', 'ubicacion', 'anio_construccion', 'imagen', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Castillo Wulff'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Viña del Mar, Región de Valparaíso'}),
            'anio_construccion': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 1906'}),
            'imagen': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://ejemplo.com/foto.jpg'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Historia y características...'}),
        }