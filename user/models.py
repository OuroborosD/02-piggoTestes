from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.


class Create(models.Model):
    usuario = models.CharField(max_length=30)
    senha = models.CharField(max_length=20)

    