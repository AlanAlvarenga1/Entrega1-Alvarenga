from django.db import models

# Create your models here.

class Lector(models.Model):
    nombre_anonimo=models.CharField(max_length=30)
    pais_de_residencia=models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.nombre_anonimo}'

class Bloggero(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    alias=models.CharField(max_length=30)
    pais_de_residencia=models.CharField(max_length=30)
    correo_electronico=models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.alias}'

class Empresa(models.Model):
    nombre_de_empresa=models.CharField(max_length=30)
    rubro=models.CharField(max_length=30)
    cuit=models.IntegerField()
    correo_electronico=models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.nombre_de_empresa}'    
