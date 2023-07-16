from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _

from parler.models import TranslatableModel, TranslatedFields

from user.models import CustomUser


class CourseType(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=60, unique=True),
    )

class Course(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=60, unique=True),
        description = models.TextField(null=True, blank=True),
    )

    price = models.FloatField()
    planned_time = models.IntegerField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)  
    time_update = models.DateTimeField(auto_now=True)  
    course_type = models.ForeignKey(CourseType, on_delete=models.CASCADE, related_name='type')
    user = models.ManyToManyField(CustomUser)
    image = models.ImageField(upload_to='Courses/main', null=True, blank=True)
    
class CourseDataCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=60, unique=True),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')

class CourseDataSubCategory(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=60, unique=True),
    )
    category = models.ForeignKey(CourseDataCategory, on_delete=models.CASCADE)

class CourseDataTheme(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=60, unique=True),
        content = models.TextField(null=True, blank=True)
    )
    image = models.ImageField(upload_to='Course/theme/image', null=True, blank=True)
    video = models.FileField(upload_to='Corse/theme/video', null=True, blank=True)
    extra_data = models.FileField(upload_to='Course/theme/extrainfo')
    links = models.URLField(null=True, blank=True)

class CourseThemeTask(TranslatableModel):
    translations = TranslatedFields(
        content = models.TextField()
    )
    course_theme = models.OneToOneField(CourseDataTheme, on_delete=models.CASCADE, related_name='theme')
    image = models.ImageField(upload_to='Course/theme/task/image')

class CourseThemeComment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='Course/theme/comment')
    text = models.TextField()
    subcomment = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, blank=True)

class RegisterCourseUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True, null=True)  
    time_update = models.DateTimeField(auto_now=True)  
    is_finished = models.BooleanField(default=False)
    total_mark = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], null=True, blank=True)
    proposed_time = models.DateTimeField(null=True, blank=True)
    completed_themes = models.ManyToManyField(CourseDataTheme)
    is_manager = models.BooleanField(default=False)
