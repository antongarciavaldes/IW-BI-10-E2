from django.urls import path
from . import views
from django.views.i18n import set_language

urlpatterns = [
    path('', views.index, name='index'),
    path('marcas/<int:marca_id>/', views.show_marca, name='detail'),
    path('categorias/<int:categoria_id>/', views.show_categoria, name='detail'),
    path('marcas/<int:marca_id>/coches/', views.index_coches, name='coches'),
    path('categorias/<int:categoria_id>', views.show_categoria, name='categoria'),
    path('coches/<int:coche_id>', views.show_coche, name='coche'),
    path('formulario_marca/',views.marca_form_view, name = 'marca_form'),
    path('formulario_categoria/',views.categoria_form_view, name = 'categoria_form'),
    path('formulario_coche/',views.coche_form_view, name = 'coche_form'),
    path('set-language/', views.set_language, name='set_language'),
    path('es/categoria.html', views.index_categorias, name='categoria_html'),
    path('es/marcas.html', views.index_marcas, name='marcas_html')

]
