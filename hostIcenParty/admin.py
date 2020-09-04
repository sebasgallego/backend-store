from django.contrib import admin
from .models import Product, ProductAdmin, \
    Genero, GeneroAdmin, \
    TypeProduct, TypeProductAdmin, \
    BuyProduct, BuyProductAdmin, \
    DocumentsApp, DocumentsAppAdmin, \
    StatusBuy, StatusBuyAdmin

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(TypeProduct, TypeProductAdmin)
admin.site.register(BuyProduct, BuyProductAdmin)
admin.site.register(StatusBuy, StatusBuyAdmin)
admin.site.register(DocumentsApp, DocumentsAppAdmin)