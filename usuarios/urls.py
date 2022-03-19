from django.urls import path
from . import views

urlpatterns = [
    path('',views.usuario,name='usuario'),
    
    path('registro',views.registro,name='registro'),
    path('registro/lectores',views.crear_lectores,name='crear_lectores'),
    path('registro/bloggeros',views.crear_bloggeros,name='crear_bloggeros'),
    path('registro/empresas',views.crear_empresas,name='crear_empresas'),
   
    path('busqueda',views.busqueda,name='busqueda'),
    path('busqueda/lectores',views.lista_lectores,name='lista_lectores'),
    path('busqueda/bloggeros',views.lista_bloggeros,name='lista_bloggeros'),
    path('busqueda/lectores',views.lista_empresas,name='lista_empresas'),
]