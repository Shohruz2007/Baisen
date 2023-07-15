from rest_framework import serializers
from .models import *
from parler.models import TranslatableModel, TranslatedFields

class BaseThemeSerializer(TranslatableModel):
    pass