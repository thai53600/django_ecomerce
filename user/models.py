from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class UserAccount(AbstractUser):
  address = models.CharField(max_length=100, null=True, blank=True)
  phone = models.CharField(max_length=20, null=True, blank=True)
  first_name = models.CharField(max_length=100, null=True, blank=True)
  last_name = models.CharField(max_length=100, null=True, blank=True)
  gender = models.CharField(
    max_length=6,
    choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHER', 'OTHER')]
  )