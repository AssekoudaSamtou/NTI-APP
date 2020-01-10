from django.db import models

from datetime import date, datetime

from investissement.utils import incrementer_date
from investisseur.models import Investisseur
from compte.models import Compte


class Investissement(models.Model):
	investisseur = models.ForeignKey(Investisseur, related_name='investissements', on_delete=models.CASCADE)
	montant = models.DecimalField(max_digits=10, decimal_places=2)
	date_investissement = models.DateField(default=date.today)
	date_decompte = models.DateField(default=date.today)
	duree = models.PositiveSmallIntegerField(default=1)

	def __str__(self):
		return f"investissement n° {self.id}"

	def supprimer_payements(self):
		from payement.models import Payement
		payements = Payement.objects.filter(investissement=self)
		for payement in payements:
			payement.delete()

	def generer_payements(self):
		from payement.models import Payement
		base_date = self.date_decompte
		for i in range(self.duree):

			if i + 1 == self.duree:
				montant_payement = float(self.montant) * 1.4
			else:
				montant_payement = float(self.montant) * 0.4

			base_date = incrementer_date(base_date, 30)
			payement = Payement(
				investissement=self,
				date=base_date,
				montant=montant_payement,
				status="NP"
			)

			payement.investissement = self
			payement.save()
