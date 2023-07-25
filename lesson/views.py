from django.shortcuts import render

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.db.models import Q

from baisan.permissions import IsAdminUserOrReadOnly

from .models import *
from .serializers import *


class EducationViewset(viewsets.ModelViewSet):
    queryset = Education.objects.select_related("teacher").all()
    serializer_class = EducationGetSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = Education.objects.filter(teacher_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            students_list = request.data["students"]
        except:
            students_list = []

        try:
            description = request.data["description"]
        except:
            description = None

        custom_data = {
            "name": request.data["name"],
            "teacher": request.user.id,
            "students": students_list,
            "description": description,
        }


        serializer = EducationCreateUpdateSerializer(data=custom_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        

        instance = Education.objects.filter(Q(id=kwargs['pk']) & Q(teacher_id=request.user.id)).first()

        
        if instance is None:
            print('None')
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EducationCreateUpdateSerializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.teacher.id == request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)



class LessonViewset(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related("education").all()
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):

        queryset = Lesson.objects.filter(education__teacher_id=request.user.id)

        serializer = self.get_serializer(queryset, many=True)



        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        try:
            description = request.data["description"]
        except:
            description = None

        custom_data = {
            "name": request.data["name"],
            "education": request.data['education'],
            "description": description,
            "planned_time": request.data['planned_time'],
        }
        print(custom_data)

        serializer = LessonCreateUpdateSerializer(data=custom_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", True)
        
        print(request.data, kwargs['pk'])
        instance = Lesson.objects.filter(Q(id=kwargs['pk']) & Q(education__teacher_id=request.user.id)).first()
        print(instance)
        
        if instance is None:
            print('None')
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = LessonCreateUpdateSerializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.teacher.id == request.user.id:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

class LessonRequestViewset(viewsets.ModelViewSet):
    queryset = LessonRequest.objects.all()
    serializer_class = LessonRequestSerializer
    permission_classes = (IsAuthenticated,)