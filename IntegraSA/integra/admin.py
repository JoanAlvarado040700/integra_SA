from django.contrib import admin
from .models import Categoria, Publicaciones, Departamento



# Register your models here.

class anuncio(admin.ModelAdmin):
    list_display = ("titulo","id")


admin.site.register(Publicaciones, anuncio)
admin.site.register(Categoria)
admin.site.register(Departamento)

