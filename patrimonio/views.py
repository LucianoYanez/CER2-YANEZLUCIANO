from django.shortcuts import render, get_object_or_404
from .models import Categoria, LugarPatrimonial

# Create your views here.
def inicio(request):
    #Página principal
    total_lugares = LugarPatrimonial.objects.count()
    total_categorias = Categoria.objects.count()

    contexto = {
        'total_lugares': total_lugares,
        'total_categorias': total_categorias,
    }
    return render(request, 'patrimonio/inicio.html', contexto)

def catalogo(request, categoria_id=None):
    #Catalogo con filtro por categoría
    categorias = Categoria.objects.all()
    categoria_seleccionada = None

    lugares = LugarPatrimonial.objects.select_related('categoria').all()
    if categoria_id:
        categoria_seleccionada = get_object_or_404(Categoria, pk=categoria_id)
        lugares = lugares.filter(categoria=categoria_seleccionada)

    contexto = {
        'lugares': lugares,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
    }
    return render(request, 'patrimonio/catalogo.html', contexto)

def detalle_lugar(request, pk):
    #Información detallada de un lugar patrimonial
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    contexto = {
        'lugar': lugar,
    }
    return render(request, 'patrimonio/detalle.html', contexto)

def lista_categorias(request):
    #Lista de todas las categorías
    categorias = Categoria.objects.all()
    contexto = {
        'categorias': categorias,
    }
    return render(request, 'patrimonio/categorias.html', contexto)