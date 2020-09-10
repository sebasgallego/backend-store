from django.db import models
from django.contrib import admin


# Create your models here.


class TypeProduct(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.name


class TypeProductAdmin(admin.ModelAdmin):
    model = TypeProduct
    list_display = ['name']


class Genero(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.name


class GeneroAdmin(admin.ModelAdmin):
    model = Genero
    list_display = ['name']


class ProductManager(models.Manager):
    def get_by_natural_key(self, title):
        return self.get(title=title)


class Product(models.Model):
    file_img_home = models.FileField(upload_to='documents/img/', null=True, blank=True)
    file_img_2 = models.FileField(upload_to='documents/img/', null=True, blank=True)
    file_img_3 = models.FileField(upload_to='documents/img/', null=True, blank=True)
    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=100, default='')
    description = models.TextField(max_length=300)
    value = models.IntegerField()
    type_store = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1)
    type_product = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, default=1)
    material = models.CharField(max_length=100, default='')
    color = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    sizes_list = models.TextField(max_length=50, default='[S,M,L]')
    is_active = models.BooleanField(default=True)
    objects = ProductManager()

    def __str__(self):
        return "%s" % self.title

    class Meta:
        unique_together = ['title']

    def natural_key(self):
        return self.title


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['title', 'subTitle']


class StatusBuyManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class StatusBuy(models.Model):
    name = models.CharField(max_length=100)
    objects = StatusBuyManager()

    def __str__(self):
        return "%s" % self.name

    class Meta:
        unique_together = ['name']

    def natural_key(self):
        return self.name


class StatusBuyAdmin(admin.ModelAdmin):
    model = StatusBuy
    list_display = ['name']


class OrdersProduct(models.Model):
    is_finish = models.BooleanField(default=False)
    phone_contact = models.CharField(max_length=100)
    name_contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    type_house = models.CharField(max_length=100)
    units = models.IntegerField(default=1)
    value = models.CharField(max_length=100, default="0")
    size = models.CharField(max_length=100, default="None")
    file_img_home = models.CharField(max_length=100, default="None")
    status_buy = models.ForeignKey(StatusBuy, on_delete=models.CASCADE, default=1)
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE, default=1)
    file_img_bill = models.FileField(upload_to='documents/bill/', null=True, blank=True)


class OrdersProductAdmin(admin.ModelAdmin):
    model = OrdersProduct
    list_display = ['address', 'get_product', 'value', 'name_contact', 'phone_contact', 'get_status']

    def get_status(self, obj):
        return obj.status_buy.name

    get_status.short_description = 'StatusBuy'
    get_status.admin_order_field = 'status_buy__name'

    def get_product(self, obj):
        return obj.product_name.title

    get_product.short_description = 'Product'
    get_product.admin_order_field = 'product_name__title'


class DocumentsApp(models.Model):
    name = models.CharField(max_length=100)
    file_document = models.FileField(upload_to='documents/documents/', null=True, blank=True)


class DocumentsAppAdmin(admin.ModelAdmin):
    model = StatusBuy
    list_display = ['name']
