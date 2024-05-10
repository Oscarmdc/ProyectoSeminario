from django.forms import ModelForm
from ubicacion.models import Ubicaciones

class FormUbicacion(ModelForm):
    class Meta:
        model = Ubicaciones
        fields = '__all__'