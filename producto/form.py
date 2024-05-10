from django.forms import ModelForm
from producto.models import Productos

class FormProductos(ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'