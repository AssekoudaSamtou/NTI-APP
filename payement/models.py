from datetime import date

from django.db import models

from investissement.models import Investissement

STATUS_CHOICES = [
    ('NP', 'Non Payé'),
    ('PY', 'Payé'),
]


class Payement(models.Model):
    investissement = models.ForeignKey(Investissement, related_name='payements', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    montant = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __repr__(self):
        return f"Payement n° {self.id}"
