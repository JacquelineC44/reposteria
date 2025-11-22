from django.db import models
from .promocion import PROMOCION

class PRODUCTO(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    stock = models.IntegerField(default=0)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)

    promocion = models.OneToOneField(PROMOCION, on_delete=models.CASCADE, related_name="producto", null = True, blank=True)

    @property
    def disponible(self):
        return self.stock > 0  # CS13

    def __str__(self):
        return f"{self.nombre}"
    
    def aplicarPromocion(self):
        promo = self.promocion
        if promo is None:
            return self.precioUnitario
        if promo.status == 'ACTIVA':
            return self.precioUnitario * (1 - promo.descuento)
        return self.precioUnitario
    

# ==== ESPECIALIZACIONES ====

class PASTEL(models.Model):
    producto = models.OneToOneField(PRODUCTO, on_delete=models.CASCADE, primary_key=True)
    relleno = models.CharField(max_length=20)      # CS11
    sabor = models.CharField(max_length=20)        # CS8
    decoracion = models.CharField(max_length=20)   # CS9

    def __str__(self):
        return f"Pastel ({self.producto.nombre})"


class TARTA(models.Model):
    producto = models.OneToOneField(PRODUCTO, on_delete=models.CASCADE, primary_key=True)
    tamaño = models.CharField(max_length=20)       # CS10

    def __str__(self):
        return f"Tarta ({self.producto.nombre})"


class POSTRE(models.Model):
    producto = models.OneToOneField(PRODUCTO, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Postre ({self.producto.nombre})"


class PAN(models.Model):
    producto = models.OneToOneField(PRODUCTO, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return f"Pan ({self.producto.nombre})"
