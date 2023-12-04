from django import forms
from .models import Marca, Categoria, Coche

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['nombre']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = ['modelo','precio','marca','categorias'] 
        