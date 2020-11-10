from django.shortcuts import render
from .models import Cat
from .forms import CatForm
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
