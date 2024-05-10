from django.forms import ModelForm
from categoria.models import Categorias

class FormCategoria(ModelForm):
    class Meta:
        model = Categorias
        fields = '__all__'