from django.shortcuts import render

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from baisan.permissions import IsAdminUserOrReadOnly

from .models import *
from .serializers import *

class GroupConversation(viewsets.ModelViewSet):
    queryset = GroupConversation.objects.select_related('initiator').all()
    serializer_class = GroupConversationSerializer
    
    def create(self, request, *args, **kwargs):
        new_data = {'theme': request.data['theme'], 'initiator':request.user.id}

        serializer = GroupConversationCreateSerializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PrivateConversation(viewsets.ModelViewSet):
    queryset = PrivateConversation.objects.select_related('initiator').all()
    serializer_class = PrivateConversationSerializer
    
    def create(self, request, *args, **kwargs):
        new_data = {'initiator': request.user.id, 'reciever':request.data['reciever']}

        serializer = PrivateConversationCreateSerializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class PrivateMessage(viewsets.ModelViewSet):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = (IsAuthenticated,)