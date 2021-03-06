from django.db import models
from django.utils import timezone

from compte.models import Compte

TYPE_OPERATION = [
    ('Retrait', 'RETRAIT'),
    ('Depot', 'DEPOT')
]


class Operation(models.Model):
    type_operation = models.CharField(max_length=7, choices=TYPE_OPERATION)
    compte = models.ForeignKey(Compte, related_name="operations", on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f"Operation n° {self.id}"

    def __str__(self):
        return f"Operation n° {self.id}"
