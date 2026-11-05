from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/categoria/<int:categoria_id>/', views.catalogo, name='catalogo_categoria'),
    path('lugar/<int:pk>/', views.detalle_lugar, name='detalle_lugar'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
]