from django.contrib.auth.models import User
from django.db import models


class Tradeur(User):
    telephone = models.CharField(max_length=20, unique=True)
    sexe = models.CharField(max_length=1)
    avatar = models.ImageField(upload_to="photos/", null=True, blank=True)
