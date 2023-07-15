from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _

class VerificationModel(models.Model):
    username = models.CharField(max_length=150,) # Логин
    email = models.EmailField(unique=True,
                              error_messages={
                               "unique": _("A user with that email already exists."),
                                },)
    password = models.CharField(max_length=235)
    verify_code = models.IntegerField()
    
    def __str__(self) -> str:
        return self.email


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150,) 
    image = models.ImageField(upload_to='Users', null=True, blank=True)  
    email = models.EmailField(unique=True,
                              error_messages={
                               "unique": _("A user with that email already exists."),
                                },)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    birthday = models.DateField(null=True, blank=True)
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )
    time_create = models.DateTimeField(auto_now_add=True, null=True)  # time when car has created
    time_update = models.DateTimeField(auto_now=True)  # time when car has updated
    is_staff = models.BooleanField(_("staff user"), default=False)
    balance = models.FloatField(null=True, blank=True)
    adress = models.CharField(max_length=155, null=True, blank=True)
    description = models.CharField(max_length=350, null=True, blank=True)


    ordering = ('email',)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = "email"

    class Meta:
        ordering = ['id']
        verbose_name = "Пользовател"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

