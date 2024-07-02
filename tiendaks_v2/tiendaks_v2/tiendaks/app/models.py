from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    desc = models.TextField()
    fecha_crea = models.DateTimeField(default=timezone.now)
    precio = models.PositiveIntegerField()
    disp = models.BooleanField(default=True)
    img_prod = models.ImageField(default='')
    
    def __str__(self):
        return self.nombre
    
class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='img', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='productos/')
    
    def __str__(self):
        return f'Imagen de {self.producto.nombre}'

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    fecha_crea = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    
    def total(self):
        return sum(item.subtotal() for item in self.items.all())
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    def subtotal(self):
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f"Item de {self.producto.nombre} en {self.carrito}"
    
    