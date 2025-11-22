from django.contrib import admin
from .models import (
    USUARIO,
    PRODUCTO, PASTEL, TARTA, POSTRE, PAN,
    ENTREGA,
    CARRITO, DETALLE,
    ORDEN,
    TICKET,
    PROMOCION
)

admin.site.register(USUARIO)
admin.site.register(PRODUCTO)
admin.site.register(PASTEL)
admin.site.register(TARTA)
admin.site.register(POSTRE)
admin.site.register(PAN)
admin.site.register(ENTREGA)
admin.site.register(CARRITO)
admin.site.register(DETALLE)
admin.site.register(ORDEN)
admin.site.register(TICKET)
admin.site.register(PROMOCION)
