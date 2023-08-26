from apps.cactus.models import Plant
from rest_framework import serializers


class PlantsSerializers(serializers.ModelSerializer):
    
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
        
        