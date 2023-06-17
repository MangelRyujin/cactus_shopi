from apps.cactus.models import Plant
from rest_framework import serializers
from apps.pedido.models import Items_Pedido



class CarSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Items_Pedido
        fields = '__all__'

    
    