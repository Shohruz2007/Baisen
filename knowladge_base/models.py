from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import CustomUser

class BaseTheme(models.Model):
    name = models.CharField(_("theme"), max_length=50)

class KnowladgeBase(models.Model):
    name = models.CharField(_("topic"), max_length=50)
    description = models.TextField()
    image = models.ImageField(_("image"), upload_to='Knowladge_base_images',)
    link = models.URLField(null=True, blank=True)
    theme = models.ForeignKey('BaseTheme', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)