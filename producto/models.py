from django.db import models
from proveedor.models import Proveedores
from categoria.models import Categorias
from ubicacion.models import Ubicaciones


# Create your models here.

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()
    fecha_modificacion = models.DateField(auto_now=True)

    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    ubicacion = models.ForeignKey(Ubicaciones, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True)
