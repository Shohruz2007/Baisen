from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'basetheme', BaseThemeViewset , basename='basetheme')
router.register(r'knowladgebase', KnowladgeBaseViewset , basename='knowladgebase')
router.register(r'questions', FAQViewset , basename='questions')

urlpatterns = [
    path('', include(router.urls)),
]