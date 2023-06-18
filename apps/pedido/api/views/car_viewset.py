
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.cactus.models import Plant
from rest_framework.decorators import action
from apps.pedido.car import Car


class CarViewSet(viewsets.GenericViewSet):
    
    
    def list(self,request,*args,**kargs):
        car = Car(request)
        if car.car != {}:
            return Response({'order_items':car.car},status=status.HTTP_200_OK)
            
        else:
            return Response({'carro':'Carro vacio'},status=status.HTTP_200_OK)
        
        
        
    @action(detail = False, methods = ['get'])
    def add_car(self,request):
        car = Car(request)
        plant_id = self.request.query_params.get('plant_id')
        plant = Plant.objects.filter(id = plant_id).first()
        if plant:
            car.add(request = request.data,plant=plant) 
            return Response({'order_items':car.car},status=status.HTTP_200_OK)
        return Response({'error':'No estas enviando la información'},status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail = False, methods = ['delete'])
    def carro_remove_item(self,request):
        car = Car(request)
        plant_id = self.request.query_params.get('plant_id')
        plant = Plant.objects.filter(id = plant_id).first()
        car.decrement(plant)
        return Response({'order_items':car.car},status=status.HTTP_200_OK)
    

    @action(detail = False, methods = ['delete'])
    def carro_limpiar(self,request):
        car = Car(request)
        car.clear()
        return Response({'car':'Carro limpiado'},status=status.HTTP_200_OK)