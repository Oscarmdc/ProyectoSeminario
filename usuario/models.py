from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)