from django.db import models
from .usuario import USUARIO
from .carrito import CARRITO

class ORDEN(models.Model):
    idOrden = models.CharField(primary_key=True, max_length=5)

    usuario = models.ForeignKey(USUARIO, on_delete=models.CASCADE, related_name="ordenes")
    carrito = models.ForeignKey(CARRITO, on_delete=models.CASCADE, related_name="ordenes")

    def __str__(self):
        return f"Orden {self.idOrden}"
