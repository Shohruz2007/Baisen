from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(
    r"registed_course", RegisterCourseUserViewset, basename="registed_course"
)
router.register(r"type", CourseTypeViewset, basename="type")
router.register(r"main", CourseViewset, basename="main")
router.register(r"category", CourseDataCategoryViewset, basename="category")
router.register(r"subcategory", CourseDataSubCategoryViewset, basename="subcategory")
router.register(r"theme", CourseDataThemeViewset, basename="theme")
router.register(r"theme_task", CourseThemeTaskViewset, basename="cheme_task")
router.register(r"theme_comment", CourseThemeCommentView, basename="theme_comment")

urlpatterns = [
    path("", include(router.urls)),
]
