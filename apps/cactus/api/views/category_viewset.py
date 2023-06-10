from apps.cactus.api.serializers.category_serializers import CategoySerializers
import django.db
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

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
            return Response(categorys_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existen categorias'}, status= status.HTTP_200_OK)
    
    def create(self,request,*args, **kargs):
        category_serializers = self.serializer_class(data = request.data)
        if category_serializers.is_valid():
            category_serializers.save()
            return Response({'message':'Categoria creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'errors':category_serializers.errors}, status= status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk = None):
        
        categorys = self.get_queryset(pk)
        if categorys:
            categorys_serializers = self.serializer_class(categorys)
            return Response(categorys_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe la categoria'}, status= status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        
        if self.get_queryset(pk):
            category_serializer = self.serializer_class(self.get_queryset(pk) ,data = request.data)
            if category_serializer.is_valid():
                category_serializer.save()
                return Response({'message':'Categoría editada correctamente!'}, status = status.HTTP_200_OK)
            else:
             return Response(category_serializer.errors,status = status.HTTP_400_BAD_REQUEST) 
        return Response({'message':'No existe la categoría que desea editar!'},status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        
        category = self.get_queryset(pk)
        if category:
            category.delete()
            return Response({'message':'La categoría ha sido eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe la categoría que desea eliminar!'},status = status.HTTP_400_BAD_REQUEST)
