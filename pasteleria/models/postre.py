from django.db import models
from .producto import PRODUCTO
class POSTRE(models.Model):
    idPostre = models.OneToOneField(
        PRODUCTO,
        on_delete=models.CASCADE,
        primary_key=True,
        limit_choices_to={"tipo": "POSTRE"},  # opcional pero ayuda
    )
    nombrePostre = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"Postre ({self.idPostre})"