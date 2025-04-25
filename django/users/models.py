from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('project_manager', 'Project Manager'),
        ('project_lead', 'Project Lead / Tech Lead'),
        ('developer', 'Developer'),
        ('client', 'Client / Customer'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return self.username
