from django.urls import path, include
from . import views

urlpatterns = [

    # listar las carreras de la bd


    #Categorias
    path('add_cat', views.CatCreate.as_view(), name="add_cat"),
    
    path('listar_cat/', views.CatList.as_view(), name='listar_cat'),


    path('edit_cat/<int:pk>', views.CatUpdate.as_view(), name='edit_cat'),

    path('del_cat/<int:pk>', views.CatDelete.as_view(), name='del_cat'),

    #Pymes
    path('add_pyme/', views.PymeCreate.as_view(), name='add_pyme'),

    path('listar_pyme/', views.PymeList.as_view(), name='listar_pyme'),


    path('edit_pyme/<int:pk>', views.PymeUpdate.as_view(), name='edit_pyme'),

    path('del_pyme/<int:pk>', views.PymeDelete.as_view(), name='del_pyme'),
]

