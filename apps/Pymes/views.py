from django.shortcuts import render
from .models import Cat, Pyme, Producto
from .forms import CatForm, PymeForm, ProductoForm
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse

# Create your views here.


# Categorías


class CatCreate(CreateView):
    model = Cat
    form_class = CatForm
    template_name = 'Pymes/cat_form.html'
    success_url = reverse_lazy("listar_cat")


class CatList(ListView):
    model = Cat
    template_name = 'Pymes/listar_cat.html'
    # paginate_by = 4

class MostrarCategorias(ListView):
    model = Cat
    template_name = 'Pymes/categorias.html'


def filtro_pyme(request, pk):
    pymes = Pyme.objects.filter(cat_id=pk)
    return render(request, "Pymes/filtrar_categoria.html", {'pymes': pymes})


def pymes(request, pk):
    pymes = get_object_or_404(Pyme, pk=pk)
    prod = Producto.objects.filter(pyme_id=pk)
    return render(request, 'Pymes/pagina_pyme.html', {'pymes': pymes, 'prod': prod})

class CatUpdate(UpdateView):
    model = Cat
    form_class = CatForm
    template_name = 'Pymes/cat_form.html'
    success_url = reverse_lazy('listar_cat')


class CatDelete(DeleteView):
    model = Cat
    template_name = 'Pymes/cat_delete.html'
    success_url = reverse_lazy('listar_cat')

#Pymes
class PymeCreate(CreateView):
    model = Pyme
    form_class = PymeForm
    template_name = 'Pymes/Pyme_form.html'
    success_url = reverse_lazy("listar_pyme")


class PymeList(ListView):
    model = Pyme
    template_name = 'Pymes/listar_pyme.html'
    # paginate_by = 4


class PymeUpdate(UpdateView):
    model = Pyme
    form_class = PymeForm
    template_name = 'Pymes/Pyme_form.html'
    success_url = reverse_lazy('listar_pyme')


class PymeDelete(DeleteView):
    model = Pyme
    template_name = 'Pymes/Pyme_delete.html'
    success_url = reverse_lazy('listar_pyme')

#productos
class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Pymes/producto_form.html'
    success_url = reverse_lazy("listar_producto")


class ProductoList(ListView):
    model = Producto
    template_name = 'Pymes/listar_producto.html'
    # paginate_by = 4


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Pymes/producto_form.html'
    success_url = reverse_lazy('listar_producto')


class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'Pymes/producto_delete.html'
    success_url = reverse_lazy('listar_producto')


class SearchResultsView(ListView):
    model = Pyme
    template_name = 'Pymes/search.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Pyme.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query))
        
        return object_list