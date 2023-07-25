from django.db import models

from django.utils.translation import gettext as _
from user.models import CustomUser

from parler.models import TranslatableModel, TranslatedFields

class BaseTheme(TranslatableModel):
    translation = TranslatedFields(
        name = models.CharField(_("theme"), max_length=100, unique=True),
    )

    class Meta:
        ordering = ['id']
        verbose_name = "Категории для тем"
        verbose_name_plural = "Категория для тем"
        

class KnowladgeBase(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, null=True, blank=True),
        description = models.TextField(null=True, blank=True),
    )

    image = models.ImageField(_("image"), upload_to='Knowladge_base_images', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    theme = models.ForeignKey('BaseTheme', on_delete=models.SET_NULL, null=True, blank=True, related_name='theme')
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Темы"
        verbose_name_plural = "Тема"
        
class FAQModel(models.Model):
    question = models.TextField()
    answer = models.TextField()