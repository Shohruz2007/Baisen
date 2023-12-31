from rest_framework import serializers
from .models import *


class VerificationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VerificationModel
        fields = ['username', 'email', 'verify_code','password']
    
    

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id", "username", "password", "email"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','image','phone_number','birthday','balance','adress','description']

class UserBaseInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'image']

class ConnectToUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectToUser
        fields = ['id', 'email', 'phone_number', 'comment']