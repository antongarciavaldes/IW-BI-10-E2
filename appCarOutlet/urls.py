from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_marcas, name='index'),
    path('marcas/<int:marca_id>/', views.show_marca, name='detail'),
    path('marcas/<int:marca_id>/coches/', views.index_coches, name='coches'),
    path('categorias/<int:categoria_id>', views.show_categoria, name='categoria'),
    path('coches/<int:coche_id>', views.show_coche, name='coche'),
]
