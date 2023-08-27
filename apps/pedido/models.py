from django.db import models
from apps.cactus.models import Plant
from apps.users.models import User
# from django.core.validators import MinLengthValidator
# Create your models here.



class Order(models.Model):
    """Model definition for Order."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User',blank=False, null= False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Pedido realizado por el usuario {self.user.name} {self.user.last_login}'

class Items_Order(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, verbose_name='Plant',blank=False, null= False)
    order= models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Order',blank=False, null= False)
    cost = models.DecimalField('Costo', max_digits=10,  decimal_places=2, blank= False, null= False)
    qty = models.PositiveIntegerField('Quantity', default= 1 ,blank= False, null= False  )
    
    class Meta:
        """Meta definition for Items Order."""

        verbose_name = 'Item Order'
        verbose_name_plural = 'Items Order'

    def __str__(self):
        return f'Item {self.plant.name} de la orden {self.order}'