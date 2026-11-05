from django.contrib import admin

# Register your models here.
from .models import Categoria, LugarPatrimonial

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(LugarPatrimonial)
class LugarPatrimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'ubicacion', 'anio_construccion')
    search_fields = ('nombre', 'ubicacion')
    list_filter = ('categoria',)
    list_per_page = 10