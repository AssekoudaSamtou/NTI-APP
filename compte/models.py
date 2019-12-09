from django.db import models
from django.db.models import ManyToManyField
from django.urls import reverse

from broker.models import Broker
from tradeur.models import Tradeur


class Compte(models.Model):
    num_compte = models.CharField(max_length=225)
    tradeur = models.ForeignKey(Tradeur, related_name='comptes', on_delete=models.CASCADE)
    broker = models.ForeignKey(Broker, related_name='comptes', on_delete=models.CASCADE)
    montant_investi = models.PositiveSmallIntegerField()

    def get_absolute_url(self):
        return reverse('comptes', kwargs={'pk': self.pk})

    def __repr__(self):
        return f"{self.num_compte}"


class Exercice(models.Model):
    date_debut = models.DateField()
    duree = models.PositiveSmallIntegerField(default=5)
    balance_initialisation = models.IntegerField()
    objectif = models.PositiveSmallIntegerField(default=100)
    mois = ManyToManyField(
        'Compte',
        through='ExerciceCompte',
        through_fields=('exercice', 'compte')
    )

    def __repr__(self):
        return f"{self.id}"


class Mois(models.Model):
    numero = models.CharField(max_length=30)
    balance_debut = models.DateField()
    balance_courante = models.IntegerField()
    exercice = models.ForeignKey('ExerciceCompte', related_name='mois', on_delete=models.DO_NOTHING)

    def __repr__(self):
        return f"{self.numero}"


class ExerciceCompte(models.Model):
    exercice = models.ForeignKey('Exercice', on_delete=models.DO_NOTHING)
    compte = models.ForeignKey('Compte', on_delete=models.DO_NOTHING)
