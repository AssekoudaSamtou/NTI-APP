from django.db import models
from django.contrib.auth.models import User

from tradeur.models import Personne


class Commercial(Personne):

    def __repr__(self):
        return f"{self.nom}"

    def __str__(self):
        return f"{self.nom} {self.prenom}"
