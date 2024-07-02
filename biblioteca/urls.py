from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import inicio, tienda, quienesSomos, trabajaConNosotros, reservaTuGas, cotizarPrecio,disponibilidad


urlpatterns = [
    path('', inicio, name='inicio'),
    path('tienda', tienda, name='tienda'),
    path('quienesSomos', quienesSomos, name='quienesSomos'),
    path('trabajaConNosotros', trabajaConNosotros, name='trabajaConNosotros'),
    path('reservaTuGas', reservaTuGas, name='reservaTuGas'),
    path('cotizarPrecio', cotizarPrecio, name='cotizarPrecio'),
    path('disponibilidad', disponibilidad, name='disponibilidad'),
    path('perfil/', views.ver_perfil, name='perfil'),
    #PESTAÑAS



    #CRUD
    path('productos', views.productos, name="productos"),
    path('crear', views.crear, name="crear"),
    path('detalle<id>', views.detalle, name="detalle"),
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar/<id>/', views.eliminar, name="eliminar"),




    #LOGINSSS Y REGISTER
    path('registrar/', views.registrar, name="registrar"),
    path('logout/', views.cerrar, name="cerrar"),
    path('login/', auth_views.LoginView.as_view(), name='login'),




    #TIENDAAAKARMLAN
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('eliminar_producto/<id>', views.eliminar_producto, name="eliminar_producto"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_carrito, name="limpiar"),
    path('generarBoleta/', views.generar_boleta, name='generarBoleta'),
   




]