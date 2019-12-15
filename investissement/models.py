from django.db import models

from datetime import date, datetime

from investisseur.models import Investisseur
from compte.models import Compte


class Investissement(models.Model):
	investisseur = models.ForeignKey(Investisseur, related_name='investissements', on_delete=models.DO_NOTHING)
	montant = models.DecimalField(max_digits=10, decimal_places=2)
	date_investissement = models.DateField(default=date.today)
	date_decompte = models.DateField(default=date.today)
	duree = models.PositiveSmallIntegerField(default=1)

	def __str__(self):
		return f"investissement n° {self.id}"
