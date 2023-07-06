from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','last_name','email','image','username','password')
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'name':instance.name,
            'last_name':instance.last_name,
            'username':instance.username,
            'email':instance.email,
            'image':instance.image.url if instance.image != '' else '',   
        }
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
    
        
class Password_SetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length =128,min_length =8, write_only = True)
    password2 = serializers.CharField(max_length =128,min_length =8, write_only = True)
    
    def validate(self,data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password':'Las contraseñas son incorrectas'})
        return data
    
    
        
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('username','email','name','last_name','image')


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
        return data
    
 
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')

    
class LogoutUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)