from django.db import models
from django.utils.translation import gettext as _

from parler.models import TranslatableModel, TranslatedFields

from user.models import CustomUser

class Education(models.Model):
    name = models.CharField(max_length=150)
    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='teacher')
    students = models.ManyToManyField(CustomUser, blank=True, related_name='students')
    description = models.TextField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)


class Lesson(models.Model):
    name = models.CharField(max_length=150)
    attended_students = models.ManyToManyField(CustomUser,  blank=True, related_name='attended_students')
    planned_time = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)
    education = models.ForeignKey(Education, on_delete=models.CASCADE,related_name='education')

class LessonRequest(models.Model):
    fullname = models.CharField(max_length=80)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    location = models.CharField(max_length=150)
    education = models.ForeignKey(Education, on_delete=models.CASCADE) 
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='request_owner')