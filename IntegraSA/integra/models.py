from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = ('Departamento')
        verbose_name_plural = ('Departamentos')
    def __str__(self):
        return self.nombre

class Publicaciones(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField(blank=True)
    banner = models.ImageField(blank=True,upload_to="vacante")
    salario = models.IntegerField(blank=True, null=True)
    urgencia = models.BooleanField()
    fecha_limite = models.DateTimeField(blank=True)
    #Area ira en otra tabla
    experiencia = models.IntegerField(blank=True, null=True) 
    vacantes = models.IntegerField(blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(Categoria)
    dep = models.ManyToManyField(Departamento)



    class Meta:
        verbose_name = ('Publicacion')
        verbose_name_plural = ('Publicaciones')

    def __str__(self):
        return self.titulo



