from django.contrib import admin
from .models import (
    USUARIO,
    PRODUCTO, PASTEL,
    PEDIDO, DETALLE, PROMOCION
)

admin.site.register(USUARIO)
admin.site.register(PRODUCTO)
admin.site.register(PASTEL)
admin.site.register(PROMOCION)
admin.site.register(PEDIDO)
admin.site.register(DETALLE)


