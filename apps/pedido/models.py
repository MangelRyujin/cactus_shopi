from django.db import models
from apps.cactus.models import Plant
# from django.core.validators import MinLengthValidator
# Create your models here.


# class Pedido(models.Model):
#     nombre_solicitante=models.CharField(max_length = 50,null = True)
#     apellido1_solicitante=models.CharField(max_length = 50,null = True)
#     apellido2_solicitante=models.CharField(max_length = 50,null = True)
#     carnet=models.CharField( max_length=11,validators=[MinLengthValidator(11)])
#     fecha_inicial=models.DateField(null = True)
#     email=models.EmailField(blank=True)
#     fecha_creacion = models.DateField('Fecha de creacion', auto_now = False, auto_now_add = True)
    



class Items_Pedido(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null= False, blank=False)
    quantity = models.PositiveIntegerField('Quantity',default=1)
    
    
    
    class Meta:
        """Meta definition for Items Pedido."""

        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return f'Item of {self.plant}'
    
