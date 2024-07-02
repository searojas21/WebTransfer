from django.shortcuts import render, redirect, get_object_or_404
from biblioteca.compras import Carrito
from .forms import Galon, GalonesForms, RegistroUserForm
from .models import Galon, Marca,Boleta, detalle_boleta
from django.contrib.auth import logout
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import PerfilForm



# Create your views here.
#RIP



# HTML'S DE BARRA DE NAVEGACION
def inicio(request):
    return render(request, 'index.html') 

def tienda(request):
    galones = Galon.objects.all()
    datos={
        'galones':galones
    }
    return render(request, 'tienda.html', datos)

def quienesSomos(request):
    return render(request, 'quienesSomos.html')

def reservaTuGas(request):
    return render(request, 'formulario.html')

def trabajaConNosotros(request):
    return render(request, 'formulario2.html')

def cotizarPrecio(request):
    return render(request, 'cotizarPrecio.html')

def disponibilidad(request):
    return render(request, 'disponibilidad.html')





#CRUD


def productos(request):
    galonesforms = Galon.objects.all()  # similar a select * from Galon
    return render(request, 'productos.html', {"galonesforms": galonesforms})

def crear(request):
    if request.method == 'POST':
        galonesforms = GalonesForms(request.POST, request.FILES)
        if galonesforms.is_valid():
            galonesforms.save()  # similar al insert into
            return redirect('productos')
    else:
        galonesforms = GalonesForms()
    return render(request, 'crear.html', {'galonesforms': galonesforms})

def detalle(request, id):
    galon = get_object_or_404(Galon, idGalon=id)  # buscamos un objeto por medio del id
    return render(request, 'detalle.html', {'galon': galon})

def modificar(request, id):
    galon = Galon.objects.get(idGalon=id)
    if request.method == 'POST':
        form = GalonesForms(request.POST, request.FILES, instance=galon)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = GalonesForms(instance=galon)
    
    datos = {
        'forModificar': form,
        'galon': galon
    }
    return render(request, 'modificar.html', datos)

def eliminar(request, id):
    galon = get_object_or_404(Galon, idGalon=id)
    if request.method == 'POST':
        galon.delete()
        return redirect('productos')
    return render(request, 'eliminar.html', {'galon': galon})





#LOGIN - REGISTRO - CERRAR


def cerrar(request):
    logout(request)
    return redirect('inicio')

def registrar(request):
    data={                          #parámetro que llega al template
        'form': RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()       #crear un objeto en el backend
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('inicio') 
        data["form"]=formulario           
    return render(request, 'registration/registrar.html',data)






# METODOS CRUD CARRITO

def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    galon = Galon.objects.get(idGalon=id)
    carrito_compra.agregar(galon=galon)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    galon = Galon.objects.get(idGalon=id)
    carrito_compra.eliminar(galon=galon)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra = Carrito(request)
    galon = Galon.objects.get(idGalon=id)
    carrito_compra.restar(galon=galon)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')

#BOLETAAAA


def generar_boleta(request):
    carrito = Carrito(request)
    if not carrito.carrito:
        return redirect('tienda')

    total = sum(int(item['total']) for item in carrito.carrito.values())
    nueva_boleta = Boleta(total=total)
    nueva_boleta.save()

    for item in carrito.carrito.values():
        galon = Galon.objects.get(idGalon=item['idGalon'])
        detalle = detalle_boleta(
            id_boleta=nueva_boleta,
            id_producto=galon,
            cantidad=item['cantidad'],
            subtotal=item['total']
        )
        detalle.save()

    carrito.limpiar()
    return render(request, 'detallecarrito.html', {
        'fecha': nueva_boleta.fechaCompra,
        'productos': detalle_boleta.objects.filter(id_boleta=nueva_boleta),
        'total': total,
    })




#PERFIIIIL

@login_required
def ver_perfil(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'perfil.html', context)



@login_required
def perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=request.user)

    return render(request, 'perfil.html', {'form': form})