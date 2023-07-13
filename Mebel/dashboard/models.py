from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, user_name, password, **extra_fields):
        if not user_name:
            raise ValueError("The User_name must be set")
        user_name = user_name
        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser mast have is_staff=True")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser mast have is_superuser=True")

        return self.create_user(user_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=56, blank=True)
    user_name = models.CharField(max_length=56, unique=True, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    company = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    country = models.CharField(max_length=128, null=True, blank=True)
    postal_kod = models.IntegerField(null=True, blank=True)
    about_me = models.TextField(blank=True, null=True)
    avatar = models.ImageField(null=True, blank=True)
    auf = models.CharField(max_length=90, null=True, blank=True)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.user_name


