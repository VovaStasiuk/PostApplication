from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=128, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=40, default='')
    second_name = models.CharField(max_length=40, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    difficult_password = models.PositiveSmallIntegerField(default=0)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
