from apps.cactus.api.serializers.category_serializers import CategoySerializers
import django.db
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(viewsets.GenericViewSet):
    serializer_class = CategoySerializers
    
    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def list(self, request, *args, **kargs):
        
        categorys = self.get_queryset()
        if categorys.exists():
            categorys_serializers = self.serializer_class(categorys,many = True)
            return Response({'categorys':categorys_serializers.data}, status= status.HTTP_200_OK)
        
        return Response({'message':'No existen categorias'}, status= status.HTTP_200_OK)