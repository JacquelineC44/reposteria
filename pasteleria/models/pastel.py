from django.db import models
from .producto import PRODUCTO
class PASTEL(models.Model):
    producto = models.OneToOneField(
        PRODUCTO,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={"tipo": "PASTEL"},  # opcional pero ayuda
    )
    relleno = models.CharField(max_length=20)      # CS11
    sabor = models.CharField(max_length=20)        # CS8
    decoracion = models.CharField(max_length=20)   # CS9
    tamaño = models.CharField(max_length=20)       # CS10

    def __str__(self):
        return f"Pastel ({self.producto.nombre})"