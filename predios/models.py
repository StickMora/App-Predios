from django.db import models

class Propietario(models.Model):
    TIPO_IDENTIFICACION_CHOICES = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'Número de identificación tributaria'),
        ('TI', 'Tarjeta de Identidad'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=[('Natural', 'Natural'), ('Jurídico', 'Jurídico')])
    numero_identificacion = models.CharField(max_length=20)
    tipo_identificacion = models.CharField(max_length=3, choices=TIPO_IDENTIFICACION_CHOICES)

    def __str__(self):
        return self.nombre

class Predio(models.Model):
    TIPO_CHOICES = [('Urbano', 'Urbano'), ('Rural', 'Rural')]

    nombre_o_Direccion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    numero_catastral = models.CharField(max_length=30, unique=True)
    numero_matricula = models.CharField(max_length=30, unique=True)
    propietarios = models.ManyToManyField(Propietario)

    def __str__(self):
        return self.nombre_direccion
