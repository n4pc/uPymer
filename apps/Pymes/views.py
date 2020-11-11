from django.shortcuts import render
from .models import Cat, Pyme
from .forms import CatForm, PymeForm
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


# --Otra forma usando clases Generics -------
class CatCreate(CreateView):
    model = Cat
    form_class = CatForm
    template_name = 'Pymes/cat_form.html'
    success_url = reverse_lazy("listar_cat")


class CatList(ListView):
    model = Cat
    template_name = 'Pymes/listar_cat.html'
    # paginate_by = 4


class CatUpdate(UpdateView):
    model = Cat
    form_class = CatForm
    template_name = 'Pymes/cat_form.html'
    success_url = reverse_lazy('listar_cat')


class CatDelete(DeleteView):
    model = Cat
    template_name = 'Pymes/cat_delete.html'
    success_url = reverse_lazy('listar_cat')


class PymeCreate(CreateView):
    model = Pyme
    form_class = PymeForm
    template_name = 'Pymes/Pyme_form.html'
    success_url = reverse_lazy("listar_Pyme")


class PymeList(ListView):
    model = Pyme
    template_name = 'Pymes/listar_Pyme.html'
    # paginate_by = 4


class PymeUpdate(UpdateView):
    model = Pyme
    form_class = PymeForm
    template_name = 'Pymes/Pyme_form.html'
    success_url = reverse_lazy('listar_Pyme')


class PymeDelete(DeleteView):
    model = Pyme
    template_name = 'Pymes/Pyme_delete.html'
    success_url = reverse_lazy('listar_Pyme')
