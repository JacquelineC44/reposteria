from django.db import models
from .orden import ORDEN

class TICKET(models.Model):
    idTicket = models.CharField(primary_key=True, max_length=5)

    orden = models.OneToOneField(ORDEN, on_delete=models.CASCADE, related_name="ticket")

    fecha = models.DateField()
    hora = models.TimeField()

    FORMA_PAGO = (
        ("EFECTIVO", "Efectivo"),
        ("TARJETA", "Tarjeta"),     # CS3
        ("TRANSFERENCIA", "Transferencia"),
    )
    formaPago = models.CharField(max_length=20, choices=FORMA_PAGO)

    STATUS = (
        ("ENTREGADO", "Entregado"),
        ("ENVIADO", "Enviado"),
        ("CANCELADO", "Cancelado"),  # CS1
    )
    status = models.CharField(max_length=20, choices=STATUS)

    @property
    def total(self):  # CS4: suma de los subtotales del carrito
        detalles = self.orden.carrito.detalles.all()
        return sum([d.subtotal for d in detalles])

    def __str__(self):
        return f"Ticket {self.idTicket}"
