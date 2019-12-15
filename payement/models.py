from django.db import models

from investissement.models import Investissement


class Payement(models.Model):
	investissement = models.ForeignKey(Investissement, related_name='payements', on_delete=models.CASCADE)
	date = models.CharField(max_length=20)
	montant = models.DecimalField(max_digits=10, decimal_places=2, null=False)

	def __repr__(self):
		return f"Payement n° {self.id}"
