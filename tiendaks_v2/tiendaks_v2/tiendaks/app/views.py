from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Carrito, ItemCarrito
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def nosotros(request):
    return render(request, 'app/nosotros.html')



def salir(request):
    logout(request)
    return redirect('home')


@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    total = carrito.total()
    return render(request, 'app/carrito.html', {'carrito': carrito, 'total': total})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            cantidad = form.cleaned_data['cantidad']
            item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
            if not item_created:
                item.cantidad += cantidad
                item.save()
            else:
                item.cantidad = cantidad
                item.save()
            return redirect('carrito')
    else:
        form = AgregarProductoForm()

    return render(request, 'app/agregar_al_carrito.html', {'form': form, 'producto': producto})



@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    if item.carrito.usuario == request.user:
        item.delete()
    return redirect('carrito')


@login_required
def limpiar_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    carrito.items.all().delete()
    return redirect('carrito')


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_producto')
    else:
        form = ProductoForm()
    
    return render(request, 'app/CRUD/agregar.html', {'form': form})


def listar_productos(request):
    productos = Producto.objects.all()
    form = AgregarProductoForm()
    return render(request, 'app/CRUD/listar.html', {'productos':productos, 'form':form})


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_producto")
        data["form"]= formulario
    return render(request, 'app/CRUD/modificar.html', data)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_producto")


def registro(request):
    data={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado Correctamente")
            return redirect(to="home")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)