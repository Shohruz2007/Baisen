from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('', include(router.urls)),
]