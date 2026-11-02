from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.nombre

class LugarPatrimonial(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre del lugar patrimonial')
    descripcion = models.TextField(verbose_name='Descripción')
    ubicacion = models.CharField(max_length=200, verbose_name='Ubicación (Ciudad / Comuna)')
    anio_construccion = models.PositiveIntegerField(verbose_name='Año de construcción')
    imagen = models.URLField(max_length=500, verbose_name='URL de la imagen')

    #Relacion 1 a muchos con Categoria
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='lugares',
        verbose_name='Categoría'
    )

    class Meta:
        verbose_name = 'Lugar Patrimonial'
        verbose_name_plural = 'Lugares Patrimoniales'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre