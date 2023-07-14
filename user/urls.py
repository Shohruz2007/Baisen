from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', AdminUserView, basename='user')

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('change_password/', ChangePasswordView.as_view()),
    path('user/', CurrentUserView.as_view()),
    path('', include(router.urls)),
]