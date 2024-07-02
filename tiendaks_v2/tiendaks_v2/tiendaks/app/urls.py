from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('nosotros/', nosotros, name='nosotros'),
    path('login/', login, name='login'),
    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-producto/', listar_productos, name='listar_producto'),
    path('modificar-producto/<int:id>', modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('carrito/', ver_carrito, name='carrito'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar-del-carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('limpiar-carrito/', limpiar_carrito, name='limpiar_carrito'),
    path('registro/', registro, name='registro'),
    path('logout/', salir, name='salir'),
]
