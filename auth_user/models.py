from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    theme = models.CharField(max_length=10, default='light')