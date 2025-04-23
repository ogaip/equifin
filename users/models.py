from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    METHOD_CHOICES = [
        ('50-30-20', '50-30-20'),
        ('70-20-10', '70-20-10'),
        ('80-10-10', '80-10-10'),
    ]
    metodo_preferido = models.CharField(
        max_length=10, choices=METHOD_CHOICES, default='50-30-20')

    def __str__(self):
        return self.username
