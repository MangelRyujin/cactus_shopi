from apps.cactus.models import Plant
from rest_framework import serializers



class PlantSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Plant
        fields = '__all__'

