"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

from datetime import datetime

from uploader.models import Image



class UserManager(BaseUserManager):
    """Manager for users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""
    class NacionalidadeChoices(models.IntegerChoices):
        BRASIL = 1, "Brasil"
        ESTADOS_UNIDOS = 2, "Estados Unidos"
        CANADA = 3, "Canadá"
        REINO_UNIDO = 4, "Reino Unido"
        ALEMANHA = 5, "Alemanha"
        FRANCA = 6, "França"
        JAPAO = 7, "Japão"
        CHINA = 8, "China"
        INDIA = 9, "Índia"
        AUSTRALIA = 10, "Austrália"
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    created_at = models.DateField(default=datetime.now)
    nacionalidade = models.IntegerField(choices=NacionalidadeChoices.choices, null=True, blank=True)
    linguagem_principal = models.CharField(max_length=255, null=True, blank=True)
    especializacao = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ForeignKey(Image, related_name="+", on_delete=models.CASCADE, null=True, blank=True, default=None)
    instagram = models.CharField(max_length=255, unique=True, null=True, blank=True)
    linkedin = models.CharField(max_length=255, unique=True, null=True, blank=True)
    isPro = models.BooleanField(default=False)
    passage_id = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
