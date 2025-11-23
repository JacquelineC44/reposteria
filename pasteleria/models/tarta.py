from django.db import models
from .producto import PRODUCTO
class TARTA(models.Model):
    idTarta = models.OneToOneField(
        PRODUCTO,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={"tipo": "TARTA"},  # opcional pero ayuda
    )
    nombreTarta = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"Tarta ({self.idTarta})"