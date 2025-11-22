from django.db import models
from datetime import date

class USUARIO(models.Model):
    idUsuario = models.CharField(primary_key=True, max_length=5)

    correo = models.EmailField(max_length=255, unique=True)
    nombreU = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=255)

    nombres = models.CharField(max_length=120)
    apellidoP = models.CharField(max_length=60)
    apellidoM = models.CharField(max_length=60, null=True, blank=True)

    fechaN = models.DateField()
    celular = models.CharField(max_length=20)

    puntosReco = models.IntegerField(default=0)
    saldoEqui = models.DecimalField(max_digits=10, decimal_places=2,
                                    null=True, blank=True)

    @property
    def edad(self):
        hoy = date.today()
        return hoy.year - self.fechaN.year - (
            (hoy.month, hoy.day) < (self.fechaN.month, self.fechaN.day)
        )

    def __str__(self):
        return f"{self.nombres} {self.apellidoP}"