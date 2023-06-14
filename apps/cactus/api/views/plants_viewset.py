from apps.cactus.api.serializers.plants_serializers import PlantSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.cactus.models import Plant
from rest_framework.decorators import action
from django.db.models import Q

class PlantsViewSet(viewsets.GenericViewSet):
    serializer_class = PlantSerializers

    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    def list(self, request, *args, **kargs):
        
        plants = self.get_queryset()
        if plants.exists():
            plants_serializers = self.serializer_class(plants,many = True)
            return Response(plants_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existen plantas'}, status= status.HTTP_404_NOT_FOUND)
    
    def create(self,request,*args, **kargs):
        plants_serializers = self.serializer_class(data = request.data)
        if plants_serializers.is_valid():
            plants_serializers.save()
            return Response({'message':'Planta creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'errors':plants_serializers.errors}, status= status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk = None):
        
        plants = self.get_queryset(pk)
        if plants:
            plants_serializers = self.serializer_class(plants)
            return Response(plants_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe la planta'}, status= status.HTTP_404_NOT_FOUND)
    
    def update(self,request,pk=None):
        
        if self.get_queryset(pk):
            plants_serializers = self.serializer_class(self.get_queryset(pk) ,data = request.data)
            if plants_serializers.is_valid():
                plants_serializers.save()
                return Response({'message':'Planta editada correctamente!'}, status = status.HTTP_200_OK)
            else:
             return Response(plants_serializers.errors,status = status.HTTP_400_BAD_REQUEST) 
        return Response({'message':'No existe la planta que desea editar!'},status = status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk = None):
        
        plant = self.get_queryset(pk)
        if plant:
            plant.delete()
            return Response({'message':'La planta ha sido eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe la planta que desea eliminar!'},status = status.HTTP_404_NOT_FOUND)

    
    @action(detail = False, methods = ['get'])
    def search_category(self,request):
        
        category = request.query_params.get('category')
        plants = Plant.objects.filter(
            Q(category = category)
        )
        if plants.exists():
            plants_serializer = self.serializer_class(plants,many = True)
            return Response(plants_serializer.data, status= status.HTTP_200_OK)
        else:
            return Response({'message':'No existen plantas con esa categoria'}, status= status.HTTP_404_NOT_FOUND)