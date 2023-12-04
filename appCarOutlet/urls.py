from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_marcas, name='index'),
    path('marcas/<int:marca_id>/', views.show_marca, name='detail'),
    path('marcas/<int:marca_id>/coches/', views.index_coches, name='coches'),
    path('categorias/<int:categoria_id>', views.show_categoria, name='categoria'),
    path('coches/<int:coche_id>', views.show_coche, name='coche'),
    path('formulario_marca/',views.marca_form_view, name = 'marca_form'),
    path('formulario_categoria/',views.categoria_form_view, name = 'categoria_form'),
    path('formulario_coche/',views.coche_form_view, name = 'coche_form')
]
