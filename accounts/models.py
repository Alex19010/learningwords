from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import set_random_username


class User(AbstractUser):
    username = models.CharField(verbose_name="Username", max_length=100, unique=True)
    email = models.EmailField(verbose_name="Email", unique=True)
    avatar = models.ImageField(verbose_name="Avatar", upload_to="image/", default="defaults/avatar.jpg", null=True,
                               blank=True)
    date_of_birth = models.DateField(verbose_name="Date of birth", null=True, blank=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs) -> None:
        self.username = set_random_username()
        return super().save(*args, **kwargs)

