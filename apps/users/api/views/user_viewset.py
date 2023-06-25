from apps.users.api.serializers.plants_serializers import PlantSerializers
from apps.users.api.serializers.user_serializers import UserSerializer, Password_SetSerializer, UpdateUserSerializer
from apps.users.models import User
from apps.users.utils import validate_files

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


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
    
    def retrieve(self, request, pk = None):
        
        plants = self.get_queryset(pk)
        if plants:
            plants_serializers = self.serializer_class(plants)
            return Response(plants_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe la planta'}, status= status.HTTP_404_NOT_FOUND)
    

class UserViewSet(viewsets.GenericViewSet):
    serializer_class= UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,pk = None):
        return self.serializer_class().Meta.model.objects.filter(id=pk).first()

    def list(self,request):
        pk = request.user.id
        print(request.user.id)
        user = self.get_queryset(pk)
        print(user)
        if user:
            user_serializer = self.serializer_class(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'No existe el usuario!'},status = status.HTTP_404_NOT_FOUND)

    def update(self,request,pk=None):
    
        data = validate_files(request.data, 'image', True)
        user = self.get_queryset(pk)
        if user:
            user_serializers = UpdateUserSerializer(user ,data = data)
            if user_serializers.is_valid():
                user_serializers.save()
                return Response({'message':'Usuario editado correctamente!'}, status = status.HTTP_200_OK)
            else:
             return Response({'message':'Error al editar los datos!','errors':user_serializers.errors},status = status.HTTP_400_BAD_REQUEST) 
        return Response({'message':'No existe el usuario que desea editar!'},status = status.HTTP_404_NOT_FOUND)

        
    
    
    def destroy(self, request, pk = None):
        
        user = self.get_queryset(pk)
        user_delete = User.objects.filter(id = pk).first()
        if user:
            user_delete.delete()
            return Response({'message':'El usuario ha sido eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe el usuario que desa eliminar!'},status = status.HTTP_404_NOT_FOUND)

    @action(detail = True, methods = ['post'])
    def set_password(self,request,pk=None):
        user = self.get_queryset(pk)
        password_serializer = Password_SetSerializer(data = request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'message':'Contraseña actualizada correctamente'},status = status.HTTP_200_OK)

        return Response({'message':'Error al enviar datos','error':password_serializer.errors},status = status.HTTP_400_BAD_REQUEST)
    

class UserRegisterViewSet(viewsets.GenericViewSet):
    serializer_class= UserSerializer
    
    
    def get_queryset(self,pk = None):
        return self.serializer_class().Meta.model.objects.filter(id=pk).first()

    def create(self, request):
        data = validate_files(request.data, 'image')
        serializers = self.serializer_class(data = data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Usuario creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)