from apps.cactus.api.serializers.plants_serializers import PlantSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.cactus.models import Plant
from rest_framework.decorators import action
from apps.pedido.car import Car
from apps.pedido.api.serializers.car_serializers import CarSerializers


class CarViewSet(viewsets.GenericViewSet):
    serializer_class = CarSerializers
    
    def list(self,request,*args,**kargs):
        return Response(status=status.HTTP_200_OK)
    
    @action(detail = False, methods = ['get'])
    def list_car(self,request):
        car = Car(self.request)
        if car:
            car_serializer = self.serializer_class(car)
            return Response(car_serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'carro':'No existe un carro'},status=status.HTTP_404_NOT_FOUND)
        
        
    @action(detail = False, methods = ['get'])
    def add_car(self,request):
        car = Car(self.request)
        plant_id = self.request.query_params.get('plant_id')
        plant = Plant.objects.filter(id = plant_id).first()
        if plant:
            # car.add(request,plant = plant)
            # car_serializer = self.serializer_class(request,car)
            # if car_serializer.is_valid(): 
            #     print('paso validacion')
            #     print(car_serializer.data)
            # else:
            #     print('no paso validacion')
            #     Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_200_OK)
        return Response({'error':'No estas enviando la información'},status=status.HTTP_400_BAD_REQUEST)
    
# class PlantsViewSet(viewsets.GenericViewSet):
    