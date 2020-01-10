from django.db import models
from django.contrib.auth.models import User

# from tradeur.models import Personne


class Commercial(User):
    telephone = models.CharField(max_length=20, unique=True)
    sexe = models.CharField(max_length=1)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
