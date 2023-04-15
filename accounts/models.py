from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    is_delivery = models.BooleanField(default=False)
