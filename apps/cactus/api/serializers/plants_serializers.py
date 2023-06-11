from apps.cactus.models import Plant
from rest_framework import serializers



class PlantSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Plant
        fields = '__all__'

    def to_representation(self, instance):
        return{
            'id': instance.id,
            'name' : instance.name,
            'description' : instance.description,
            'image' : instance.image.url if instance.image != '' else '',
            'cost' : instance.cost,
            'category' : instance.category.category_name,
        }
    
    
    def validate_cost(self,value):
        if value < 0:
            raise serializers.ValidationError("Debe ingresar un valor mayor que 0")
        return value