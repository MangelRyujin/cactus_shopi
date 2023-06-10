from apps.cactus.models import Category
from rest_framework import serializers



class CategoySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
