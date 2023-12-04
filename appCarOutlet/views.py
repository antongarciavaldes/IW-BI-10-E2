from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Marca, Categoria, Coche

#devuelve el listado de marcas
def index_marcas(request):
	marcas = get_list_or_404(Marca.objects.order_by('nombre'))
	context = {'lista_marcas': marcas }
	return render(request, 'index.html', context)

#devuelve los datos de una marca
def show_marca(request, marca_id):
	marca = get_object_or_404(Marca, pk=marca_id)
	context = {'marca': marca }
	return render(request, 'detail.html', context)

#devuelve los coches de una marca
def index_coches(request, marca_id):
	marca = get_object_or_404(Marca, pk=marca_id)
	coches =  marca.coche_set.all()
	context = {'marca': marca, 'coches' : coches }
	return render(request, 'coches.html', context)

#devuelve los detalles de un coche
def show_coche(request, coche_id):
	coche = get_object_or_404(Coche, pk=coche_id)
	categorias =  coche.categorias.all()
	context = { 'coche': coche, 'categorias' : categorias }
	return render(request, 'coche.html', context)

# Devuelve los detalles de una habilidad
def show_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    coches =  categoria.coche_set.all()
    context = { 'coches': coches, 'categoria' : categoria }
    return render(request, 'categoria.html', context)








