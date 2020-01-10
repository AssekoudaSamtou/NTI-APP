import datetime

from django.db import models
from django.urls import reverse

from broker.models import Broker
from tradeur.models import Tradeur


class Compte(models.Model):
    num_compte = models.CharField(max_length=225, unique=True)
    tradeur = models.ForeignKey(Tradeur, related_name='comptes', null=True, blank=True, on_delete=models.DO_NOTHING)
    broker = models.ForeignKey(Broker, related_name='comptes', on_delete=models.DO_NOTHING)
    montant_investi = models.PositiveSmallIntegerField()
    date_creation = models.DateField(default=datetime.datetime.now)

    def get_absolute_url(self):
        return reverse('comptes', kwargs={'pk': self.pk})

    def __repr__(self):
        return f"{self.num_compte}"

    def __str__(self):
        return f"{self.broker} : {self.num_compte}"


class Mois(models.Model):
    numero = models.CharField(max_length=30)
    balance_debut = models.DateField()
    balance_courante = models.IntegerField()
    compte = models.ForeignKey('exercice.ExerciceCompte', related_name='mois', on_delete=models.CASCADE)

    def __repr__(self):
        return f"{self.numero}"
