from django.db import models

class ENTREGA(models.Model):
    idEntrega = models.CharField(primary_key=True, max_length=5)

    TIPO_CHOICES = (
        ("PICKUP", "PICKUP"),
        ("DOMICILIO", "DOMICILIO"),
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    direccionEntr = models.CharField(max_length=255, null=True, blank=True)  # CS12

    def __str__(self):
        return f"Entrega {self.idEntrega} ({self.tipo})"
