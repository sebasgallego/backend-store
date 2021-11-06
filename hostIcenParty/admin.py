from django.contrib import admin
from .models import Product, ProductAdmin, \
    Genero, GeneroAdmin, \
    TypeProduct, TypeProductAdmin, \
    OrdersProduct, OrdersProductAdmin, \
    DocumentsApp, DocumentsAppAdmin, \
    StatusBuy, StatusBuyAdmin

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)
admin.site.register(OrdersProduct, OrdersProductAdmin)
admin.site.register(StatusBuy, StatusBuyAdmin)
admin.site.register(DocumentsApp, DocumentsAppAdmin)
