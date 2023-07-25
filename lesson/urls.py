from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"main", EducationViewset, basename="main")
router.register(r"lesson", LessonViewset, basename="lesson")
router.register(r"lesson_request", LessonRequestViewset, basename="lesson_request")

urlpatterns = [
    path("", include(router.urls)),
]
