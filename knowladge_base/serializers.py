from rest_framework import serializers
from .models import BaseTheme, KnowladgeBase, FAQModel
from user.serializers import UserBaseInfoSerializer

from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

class BaseThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BaseTheme
        fields = ['id', 'name']


class KnowladgeBaseSerializer(TranslatableModelSerializer):
    theme = BaseThemeSerializer()
    author = UserBaseInfoSerializer()

    class Meta:
        model = KnowladgeBase
        fields = ['name','description','image','link','theme','author','time_create','time_update',]

class FAQSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FAQModel
        fields = '__all__'