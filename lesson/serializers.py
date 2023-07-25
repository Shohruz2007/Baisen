from rest_framework import serializers

from .models import *
from user.serializers import UserBaseInfoSerializer


class EducationGetSerializer(serializers.ModelSerializer):
    teacher = UserBaseInfoSerializer()
    students = UserBaseInfoSerializer(many=True)

    class Meta:
        model = Education
        fields = "__all__"
        


class EducationCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    attended_students = UserBaseInfoSerializer(many=True)

    class Meta:
        model = Education
        fields = "__all__"

class LessonCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class LessonRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
