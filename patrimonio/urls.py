from django.urls import path
from . import views

urlpatterns = [
    #Publicas
    path('', views.inicio, name='inicio'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/categoria/<int:categoria_id>/', views.catalogo, name='catalogo_categoria'),
    path('lugar/<int:pk>/', views.detalle_lugar, name='detalle_lugar'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),

    #Privadas
    path('gestion/', views.gestion_lugares, name='gestion_lugares'),
    path('gestion/crear/', views.crear_lugar, name='crear_lugar'),
    path('gestion/editar/<int:pk>/', views.editar_lugar, name='editar_lugar'),
]