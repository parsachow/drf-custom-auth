from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

CustomUser = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'name', 'password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
                }
        }
        
    def create(self, validated_data):
        print(validated_data)
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        # token['username'] = user.username
        token['email'] = user.email
        return token
    

class CustomUserSerializer(serializers.ModelSerializer):
    # email = serializers.StringRelatedField
    class Meta:
        model = CustomUser
        fields = "__all__"