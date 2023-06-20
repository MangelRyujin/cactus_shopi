from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.api.serializers.user_serializers import CustomTokenObtainPairSerializer, CustomUserSerializer,LogoutUserSerializer
from django.contrib.auth import authenticate
from apps.users.models import User
# Create your views here.
from rest_framework.permissions import IsAuthenticated

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

    def post(self, request, *args,**kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username = username, 
            password = password
            )
        userr = User.objects.filter(username = request.data.get('username'))
        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                if user_serializer:
                    Login.delete_sessions(userr.first()) 
                    
                return Response({'token': login_serializer.validated_data.get('access'),
                                 'refresh_token':login_serializer.validated_data.get('refresh'),
                                 'user':user_serializer.data,
                                 'message':'Inicio de sesion exitoso'},status = status.HTTP_200_OK)
            return Response({'error':'Contraseña o nombre de ususario incorrecto'},status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Contraseña o nombre de ususario incorrecto'},status = status.HTTP_400_BAD_REQUEST)        

            
    def delete_sessions(user):
        all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
        if all_sessions.exists():
            for session in all_sessions:
                session_data = session.get_decoded()
                if user.id == int(session_data.get('_auth_user_id')):
                    session.delete()
    
    
class Logout(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    
    
    
    
    def post(self,request,*args,**kwargs):
        user = User.objects.filter(id = request.data.get('user',0))
        if user.exists():
            RefreshToken.for_user(user.first())
            Login.delete_sessions(user.first())
            
            return Response({'message':'Sesion cerrada correctamente!'},status = status.HTTP_200_OK) 
        return Response({'error':'No existe el usuario'},status = status.HTTP_400_BAD_REQUEST)
    
    
    
        
    def delete_sessions(user):
        all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
        if all_sessions.exists():
            for session in all_sessions:
                session_data = session.get_decoded()
                if user.id == int(session_data.get('_auth_user_id')):
                    session.delete()
    
    
