from django.urls import path, include
from . import views
from .views import SearchResultsView
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Pymes import views


urlpatterns = [

    # listar las carreras de la bd


    #Categorias
    path('add_cat', views.CatCreate.as_view(), name="add_cat"),
    
    path('listar_cat/', views.CatList.as_view(), name='listar_cat'),


    path('edit_cat/<int:pk>', views.CatUpdate.as_view(), name='edit_cat'),

    path('del_cat/<int:pk>', views.CatDelete.as_view(), name='del_cat'),

    path('categorias', views.MostrarCategorias.as_view(), name='categorias'),

    path('categorias/<int:pk>', views.filtro_pyme, name='categoria'),

    #Pymes
    path('add_pyme/', views.PymeCreate.as_view(), name='add_pyme'),

    path('listar_pyme/', views.PymeList.as_view(), name='listar_pyme'),


    path('edit_pyme/<int:pk>', views.PymeUpdate.as_view(), name='edit_pyme'),

    path('del_pyme/<int:pk>', views.PymeDelete.as_view(), name='del_pyme'),

    path('search/', SearchResultsView.as_view(), name='search_results'),
    
    #Productos
    path('add_producto/', views.ProductoCreate.as_view(), name='add_producto'),

    path('listar_producto/', views.ProductoList.as_view(), name='listar_producto'),


    path('edit_producto/<int:pk>', views.ProductoUpdate.as_view(), name='edit_producto'),

    path('del_producto/<int:pk>', views.ProductoDelete.as_view(), name='del_producto'),

    path('<int:pk>', views.pymes, name='Pymes'),


     #API rest 

    path('apiProducto/', views.API_objectsProducto.as_view()),
    path('apiProducto/<int:pk>/', views.API_objects_detailsProducto.as_view()),
    path('apiPyme/', views.API_objectsPyme.as_view()),
    path('apiPyme/<int:pk>/', views.API_objects_detailsPyme.as_view()),

]
   
   

urlpatterns = format_suffix_patterns(urlpatterns)





