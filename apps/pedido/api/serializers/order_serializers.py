from rest_framework import serializers
from apps.users.models import User
from apps.pedido.models import Order, Items_Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'order':instance.id,
            'user':instance.user.id,
            'cost':instance.cost,
        }
    
    
    def validate_cost(self,value):
        if value < 0:
            raise serializers.ValidationError("El costo debe de ser mayor que 0")
        return value
    
class ItemsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_Order
        fields = '__all__'
        
    def to_representation(self, instance):
        return {
            'plant':instance.plant.id,
            'order':instance.order.id,
            'cost':instance.cost,
            'qty':instance.qty,
        }
    
    
    def validate_cost(self,value):
        if value < 0:
            raise serializers.ValidationError("El costo debe de ser mayor que 0")
        return value
    
    