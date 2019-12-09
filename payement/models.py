from django.db import models

from investissement.models import Investissement


class Payement(models.Model):
	investissement = models.ForeignKey(Investissement, related_name='payement', on_delete=models.DO_NOTHING)
	date = models.CharField(max_length=20)

	def __repr__(self):
		return f"Payement n° {self.id}"
