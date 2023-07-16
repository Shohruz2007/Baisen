from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"user_list", AdminUserViewset, basename="user_list")
router.register(r"user_connect_with", ConnectToUserViewset, basename="user_connect_with")

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("change_password/", ChangePasswordView.as_view()),
    path("user/", CurrentUserView.as_view()),
    path("", include(router.urls)),
]
