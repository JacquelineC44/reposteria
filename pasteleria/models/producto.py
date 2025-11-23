from django.db import models
from .promocion import PROMOCION

class PRODUCTO(models.Model):
    TIPO_CHOICES = (
        ("PASTEL", "Pastel"),
        ("TARTA", "Tarta"),
        ("POSTRE", "Postre"),
        ("PAN", "Pan"),
    )

    idProducto = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=120, null=True, blank=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField(default=0)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    # ← GENERALIZACIÓN: tipo de producto, no más tablas
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    promocion = models.OneToOneField(
    PROMOCION,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="producto",
    )


    @property
    def disponible(self):
        return self.stock > 0

    def aplicarPromocion(self):
        promo = self.promocion
        if promo is None:
            return self.precioUnitario
        if promo.status == "ACTIVA":
            return self.precioUnitario * (1 - promo.descuento)
        return self.precioUnitario

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"
