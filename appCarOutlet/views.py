
from django.utils.translation import gettext as _
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .forms import MarcaForm, CategoriaForm, CocheForm
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

def set_language(request):
    if 'lang' in request.GET:
        # Obtén el idioma desde la solicitud GET
        language = request.GET['lang']
        
        # Configura el idioma seleccionado en la sesión
        request.session['django_language'] = language
    
    # Redirige a la página de origen o a una página predeterminada
    return redirect(request.META.get('HTTP_REFERER', '/'))


def marca_form_view(request):
	if request.method =='POST':
		form = MarcaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = MarcaForm()
	return render(request,'marca_form.html',{'form' : form})

def categoria_form_view(request):
	if request.method =='POST':
		form = CategoriaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = CategoriaForm()
	return render(request,'categoria_form.html',{'form' : form})


def coche_form_view(request):
	if request.method =='POST':
		form = CocheForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = CocheForm()
	return render(request,'coche_form.html',{'form' : form})






