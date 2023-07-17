from rest_framework import serializers
from user.serializers import UserBaseInfoSerializer

from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from .models import Course, CourseType, CourseThemeTask, CourseDataCategory, CourseDataSubCategory, CourseDataTheme, CourseThemeComment, RegisterCourseUser

class CourseTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseType
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    user = UserBaseInfoSerializer()
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'price', 'planned_time', 'time_create', 'time_update', 'course_type', 'user', 'image']

class CourseDataCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDataCategory
        fields = ['id','name','course',]

class CourseDataSubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDataSubCategory
        fields = ['id','name','category',]

class CourseDataThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseDataTheme
        fields = ['id','name','content','image','video','extra_data','links','subcategory']

class CourseThemeTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseThemeTask
        fields = ['id','content','course_theme','image']

class CourseThemeCommentSerializer(serializers.ModelSerializer):
    user = UserBaseInfoSerializer()
    class Meta:
        model = CourseThemeComment
        fields = ['id','user','image','text','subcomment']

class RegisterCourseUserSerializer(serializers.ModelSerializer):
    user = UserBaseInfoSerializer()
    class Meta:
        model = RegisterCourseUser
        fields = '__all__'

