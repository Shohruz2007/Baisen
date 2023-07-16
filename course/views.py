from django.shortcuts import render

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.settings import api_settings
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from baisan.permissions import IsAdminUserOrReadOnly

from .models import *
from .serializers import *

class RegisterCourseUserViewset(viewsets.ModelViewSet):
    queryset = RegisterCourseUser.objects.select_related('user').all()
    serializer_class = RegisterCourseUserSerializer
    permission_classes = (AllowAny,)

    
class CourseTypeViewset(viewsets.ModelViewSet):
    serializer_class = CourseTypeSerializer
    queryset = CourseType.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = CourseType.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class CourseViewset(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = Course.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class CourseDataCategoryViewset(viewsets.ModelViewSet):
    serializer_class = CourseDataCategorySerializer
    queryset = CourseDataCategory.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = CourseDataCategory.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class CourseDataSubCategoryViewset(viewsets.ModelViewSet):
    serializer_class = CourseDataSubCategorySerializer
    queryset = CourseDataSubCategory.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = CourseDataSubCategory.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class CourseDataThemeViewset(viewsets.ModelViewSet):
    serializer_class = CourseDataThemeSerializer
    queryset = CourseDataTheme.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = CourseDataTheme.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    
class CourseThemeTaskViewset(viewsets.ModelViewSet):
    serializer_class = CourseThemeTaskSerializer
    queryset = CourseThemeTask.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]
    @method_decorator(cache_page(90))
    
    def list(self, request, *args, **kwargs):
        accept_language='en'
        if 'Accept-Language' in request.headers:
            accept_language = str(request.headers['Accept-Language'])
            
        queryset = CourseThemeTask.objects.language(accept_language).all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CourseThemeComment(viewsets.ModelViewSet):
    queryset = CourseThemeComment.objects.all()
    serializer_class = CourseThemeCommentSerializer
    permission_classes = (IsAuthenticated,) 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}