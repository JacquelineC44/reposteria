from django.db import models
from .usuario import USUARIO
from .producto import PRODUCTO

class PEDIDO(models.Model):
    idPedido = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(USUARIO, on_delete=models.CASCADE, related_name="pedidos")
    fechaEntrega = models.DateField(null=True, blank=True)
    horaEntrega = models.TimeField(null=True, blank=True)
    direccionEntrega = models.CharField(null=True, blank=True, max_length=35)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    ENTREGA_CHOICES = (
        ("PICKUP", "pickup"),
        ("DOMICILIO", "domicilio"),
    )
    tipoEntrega = models.CharField(max_length=20, choices=ENTREGA_CHOICES)
    FORMAPAGO_CHOICES = (
        ("MERCADOPAGO", "mercadopago"),
        ("TARJETA", "tarjeta"),
    )
    formaPago = models.CharField(max_length=20, choices= FORMAPAGO_CHOICES)    
    STATUS = (
        ("RECIBIDO", "Pedido Recibido"),
        ("ELABORANDO", "En proceso de elaboración"),
        ("LISTO", "Listo para entrega"),
        ("ENVIADO", "Enviado"),
        ("ENTREGADO", "Entregado"),
        ("CANCELADO", "Cancelado"),  # CS1
    )
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f"Pedido {self.idPedido} ({self.usuario.nombres})"