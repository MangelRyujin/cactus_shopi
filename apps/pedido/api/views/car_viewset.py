
import rest_framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from apps.cactus.models import Plant
from rest_framework.decorators import action
from apps.pedido.car import Car
from rest_framework.permissions import IsAuthenticated
from apps.pedido.models import Order, Items_Order
from apps.users.models import User
from apps.pedido.api.serializers.order_serializers import OrderSerializer

class CarViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    def list(self,request,*args,**kargs):
        car = Car(request)
        print(request.user.id)
        print(str(request.auth))
        for item in car.car.values():
            print(item['cost'])
       
        if car:
            
            return Response({'order_items':car.car.values(),'qty_plants':car.qty_plants(self),'cost_car':car.cost_car(self)},status=status.HTTP_200_OK)

        return Response({'order_items':[]},status=status.HTTP_200_OK)
        
        
    @action(detail = False, methods = ['get'])
    def add_car(self,request):
        car = Car(request)
        plant_id = self.request.query_params.get('plant_id')
        plant = Plant.objects.filter(id = plant_id).first()
        if plant:
            car.add(request = request.data,plant=plant) 
            return Response({'message':'Añadido al carrito','order_items':car.car.values()},status=status.HTTP_200_OK)
        return Response({'error':'No estas enviando la información'},status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail = False, methods = ['delete'])
    def carro_remove_item(self,request):
        car = Car(request)
        plant_id = self.request.query_params.get('plant_id')
        plant = Plant.objects.filter(id = plant_id).first()
        car.decrement(plant)
        return Response({'message':'Eliminaste una planta del carrito'},status=status.HTTP_200_OK)
    

    @action(detail = False, methods = ['delete'])
    def carro_limpiar(self,request):
        car = Car(request)
        car.clear()
        return Response({'car':'Carro limpiado'},status=status.HTTP_200_OK)
    
    @action(detail = False, methods = ['post'])
    def crear_order(self,request,*args, **kargs):
        car = Car(request)
        user = User.objects.filter(id = request.user.id).first()
        order=  Order.objects.create(
            user = user,
            cost = car.cost_car(self)
        )
        
        for item in car.car.values():
            plant = Plant.objects.filter(id = item['plant_id']).first()
            Items_Order.objects.create(
            plant = plant,
            order = order,
            cost = item['cost'],
            qty = item['qty'],
            )
        car.clear()
        return Response({'message':'Compra realizada'},status=status.HTTP_200_OK)
    
    
    
    @action(detail = False, methods = ['post'])
    def create_order(self,request,list,*args, **kargs):
        cost_max = 0
        for plant_id in list:
            plant = User.objects.filter(id = plant_id).first()
            cost_max+= plant.cost
        
        user = User.objects.filter(id = request.user.id).first()
        order=  Order.objects.create(
            user = user,
            cost = cost_max
        )
        
        
            
        
        for plant_id in list:
            plant = Plant.objects.filter(id = plant_id).first()
            Items_Order.objects.create(
            plant = plant,
            order = order,
            )
        serializers= self.serializer_class(order)   
        if serializers.is_valid():
            
            return Response({'message':'Compra realizada', 'order':serializers.data},status=status.HTTP_200_OK)
        
        return Response({'error':'Error al realizar la compra','order': serializers.errors},status = status.HTTP_400_BAD_REQUEST)
