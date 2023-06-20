from django.contrib import admin

from apps.pedido.models import *
# Register your models here.

admin.site.register(Order)
admin.site.register(Items_Order)