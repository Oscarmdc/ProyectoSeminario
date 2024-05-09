from django.db import models


# Create your models here.

class Ubicaciones(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre}"
