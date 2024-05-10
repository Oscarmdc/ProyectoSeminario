from django.forms import ModelForm, EmailInput
from proveedor.models import Proveedores

class FormProveedor(ModelForm):
    class Meta:
        model = Proveedores
        fields = '__all__'