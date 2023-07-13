from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate, login
from django.core.mail import send_mail
from django.conf import settings

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAdminUser, IsAuthenticated
from baisan.permissions import IsAdminUserOrReadOnly

import string
import random

from .models import *
from .serializers import *



class RegisterAPIView(CreateAPIView):
    queryset = CustomUser.objects.all()
    http_method_names = ["post"]
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def send_email(self, data):

        email = data["email"]
        name = data["username"]
        code = data["verify_code"]
        
        message = f"""Hi {name}!. 
                    Here your verification code:{code}
                    """

        send_mail(
            "Verify_code",
            message,
            "CallToCall <support@CallToCall.ru>",
            [email],
            fail_silently=False,
        )
    
    def create_code(self, data):
        
        total = string.digits
        verify_code = "".join(random.sample(total, 6))

        data_copy = data.copy()
        data_copy.update({"verify_code":int(verify_code)})

        return data_copy


    def post(self, request, *args, **kwargs):

        code = request.query_params.get('verify_code')
        if code is not None:
            params_email = request.query_params.get('email')

            user_verification_model = VerificationModel.objects.get(email=params_email)


            if int(code) == user_verification_model.verify_code:
                register_data = {"email":user_verification_model.email,'username':user_verification_model.username,'password':user_verification_model.password}
                serializer = self.serializer_class(data=register_data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_409_CONFLICT)
        
        try:
            verification = VerificationModel.objects.filter(email=request.data['email']).first()
        except:
            verification = VerificationModel.objects.filter(email=request.query_params.get('email')).first()

        if verification or request.query_params.get('resend_code') is not None:
            data = {"username":verification.username, "email":verification.email, "password":verification.password}
            data_with_code = self.create_code(data)
            self.send_email(data_with_code)
            
            verification.verify_code = data_with_code['verify_code']
            verification.save()
            return Response(status=status.HTTP_200_OK)
        
        
        new_data = self.create_code(request.data)
        serializer_class = VerificationSerializer
        serializer = serializer_class(data=new_data)

        if serializer.is_valid(raise_exception=True):
            self.send_email(new_data)
            serializer.save()
            return Response(status=status.HTTP_200_OK,)


class LoginAPIView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            return Response(self.get_tokens_for_user(user), status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):  # getting JWT token and is_staff boolean
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        }


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = CustomUser
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
                
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
