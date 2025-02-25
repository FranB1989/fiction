from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.is_superuser:
            self.username = f"{self.name.lower()}.{self.last_name.lower()}"
        super().save(*args, **kwargs)