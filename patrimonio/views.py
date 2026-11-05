from django.shortcuts import render, get_object_or_404
from .models import Categoria, LugarPatrimonial
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Categoria, LugarPatrimonial
from .forms import LugarPatrimonialForm

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

@login_required
def gestion_lugares(request):
    #Gestión de lugares patrimoniales para usuarios autenticados
    lugares = LugarPatrimonial.objects.select_related('categoria').all()
    contexto = {
        'lugares': lugares,
    }
    return render(request, 'patrimonio/gestion.html', contexto)

@login_required
@permission_required('patrimonio.add_lugarpatrimonial', raise_exception=True)
def crear_lugar(request):
    #Crear un nuevo lugar patrimonial
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST)
        if form.is_valid():
            lugar = form.save()
            messages.success(request, f'Lugar patrimonial "{lugar.nombre}" registrado exitosamente.')
            return redirect('gestion_lugares')
    else:
        form = LugarPatrimonialForm()

    contexto = {
        'form': form,
        'accion': 'Registrar nuevo lugar patrimonial',
    }
    return render(request, 'patrimonio/formulario_lugar.html', contexto)

@login_required
@permission_required('patrimonio.change_lugarpatrimonial', raise_exception=True)
def editar_lugar(request, pk):
    #Editar un lugar patrimonial existente
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)
    if request.method == 'POST':
        form = LugarPatrimonialForm(request.POST, instance=lugar)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lugar patrimonial "{lugar.nombre}" actualizado exitosamente.')
            return redirect('gestion_lugares')
    else:
        form = LugarPatrimonialForm(instance=lugar)

    contexto = {
        'form': form,
        'accion': f'Modificar lugar patrimonial: {lugar.nombre}',
        'lugar': lugar,
    }
    return render(request, 'patrimonio/formulario_lugar.html', contexto)