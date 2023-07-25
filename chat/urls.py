from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'forum', GroupConversation , basename='forum')
router.register(r'conversation', PrivateConversation , basename='conversation')

urlpatterns = [
    path('', include(router.urls)),
]