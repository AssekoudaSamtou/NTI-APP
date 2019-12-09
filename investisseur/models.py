from django.db import models

from tradeur.models import Personne


class Investisseur(Personne):

	def __repr__(self):
		return f"{self.nom} {self.prenom}"

	def __str__(self):
		return f"{self.nom} {self.prenom}"
