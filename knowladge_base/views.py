from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from baisan.permissions import IsAdminUserOrReadOnly

from .models import BaseTheme, KnowladgeBase, FAQModel
from .serializers import BaseThemeSerializer, KnowladgeBaseSerializer, FAQSerializer

class BaseThemeViewset(viewsets.ModelViewSet):
    serializer_class = BaseThemeSerializer
    queryset = BaseTheme.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
        queryset = BaseTheme.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class KnowladgeBaseViewset(viewsets.ModelViewSet):
    serializer_class = KnowladgeBaseSerializer
    queryset = KnowladgeBase.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = KnowladgeBase.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class FAQViewset(viewsets.ModelViewSet):
    queryset = FAQModel
    serializer_class = FAQSerializer
    permission_classes = [IsAdminUserOrReadOnly]