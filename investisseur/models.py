from django.contrib.auth.models import User
from django.db import models

# from tradeur.models import Personne


class Investisseur(User):
	telephone = models.CharField(max_length=20, unique=True)
	sexe = models.CharField(max_length=1)
	parrain = models.ForeignKey('Investisseur', related_name='fieuls', on_delete=models.CASCADE, null=True, blank=True)
	init_password = models.CharField(max_length=50)

	def __repr__(self):
		return f"{self.first_name} {self.last_name}"

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
