from django.db import models

class PROMOCION(models.Model):
    idPromocion = models.CharField(primary_key=True, max_length=5)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)  # CS7 formato 0.3
    vigencia = models.DateField()
    
    STATUS = (
        ("ACTIVA", "Activa"),
        ("INACTIVA", "Inactiva"),   # CS6
    )
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f"Promoción {self.idPromocion}"
