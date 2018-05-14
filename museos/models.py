from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Museo(models.Model):
    id_entidad = models.CharField(max_length=150, default="Null")
    nombre = models.TextField(default="Null")
    descripcion_entidad = models.TextField(default="Null")
    horario = models.TextField(default="Null")
    equipamiento = models.TextField(default="Null")
    transporte = models.TextField(default="Null")
    descripcion = models.TextField(default="Null")
    accesibilidad = models.IntegerField(default=0)
    content_url = models.URLField(max_length=350, default="Null")
    nombre_via = models.CharField(max_length=50, default="Null")
    clase_vial = models.CharField(max_length=50, default="Null")
    tipo_num = models.CharField(max_length=10, default="Null")
    num = models.CharField(max_length=50, default="Null")
    planta = models.CharField(max_length=50, default="Null")
    orientacion = models.TextField(default="Null")
    localidad = models.CharField(max_length=50, default="Null")
    provincia = models.CharField(max_length=50, default="Null")
    codigo_postal = models.CharField(max_length=150, default="Null")
    barrio = models.CharField(max_length=50, default="Null")
    distrito = models.CharField(max_length=50, default="Null")
    coordenada_x = models.CharField(max_length=50, default="Null")
    coordenada_y = models.CharField(max_length=50, default="Null")
    latitud = models.CharField(max_length=50, default="Null")
    longitud = models.CharField(max_length=50, default="Null")
    telefono = models.CharField(max_length=150, default="Null")
    fax = models.CharField(max_length=100, default="Null")
    email = models.CharField(max_length=100, default="Null")

class Comentarios(models.Model):
    comentario = models.TextField(default="Null")
    museo = models.ForeignKey(Museo)

class Configuracion(models.Model):
    titulo = models.CharField(max_length=100, default="Null")
    letra_size = models.CharField(max_length=50, default="Null")
    color_fondo = models.CharField(max_length=50, default="Null")
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

class Seleccion(models.Model):
    museo = models.ForeignKey(Museo)
    usuario = models.ForeignKey(User)
    fecha = models.DateField()
