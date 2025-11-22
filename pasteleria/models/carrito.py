from django.db import models
from .usuario import USUARIO
from .producto import PRODUCTO
from .entrega import ENTREGA

class CARRITO(models.Model):
    idCarrito = models.CharField(primary_key=True, max_length=5)

    usuario = models.ForeignKey(USUARIO, on_delete=models.CASCADE, related_name="carritos")
    entrega = models.ForeignKey(ENTREGA, on_delete=models.CASCADE, related_name="carritos")

    fechaE = models.DateField(null=True, blank=True)
    horaE = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Carrito {self.idCarrito}"


class DETALLE(models.Model):
    idItem = models.CharField(primary_key=True, max_length=5)

    carrito = models.ForeignKey(CARRITO, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(PRODUCTO, on_delete=models.CASCADE, related_name="detalles")

    cantidad = models.IntegerField()

    @property
    def subtotal(self):     # CS5
        return self.producto.precioUnitario * self.cantidad

    def __str__(self):
        return f"Item {self.idItem} ({self.producto.nombre})"
