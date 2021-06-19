from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser, PermissionsMixin)

from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):

    def create_user(self, username, email, name, last_name, password, is_staff,
                    is_superuser, **extra_fields):
        user = self.model(
            username=username,
            name=name,
            email=email,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

    def create_superuser(self, username, email, name, last_name,
                         password=None, **extra_fields):
        return self.create_user(username, email, name, last_name,
                                password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField("Correo Electrónico", max_length=255, unique=True)
    name = models.CharField('Nombres', max_length=255, blank=True, null=True)
    last_name = models.CharField('Apellidos', max_length=255, blank=True, null=True)
    image = models.ImageField("Imagen de perfil", upload_to="perfil/", max_length=255,
                              null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name", "last_name"]

    def __str__(self):
        return f"{self.name}, {self.last_name}"
