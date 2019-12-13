from django.db import models
from django.db.models import ManyToManyField


class Exercice(models.Model):
    date_debut = models.DateField()
    duree = models.PositiveSmallIntegerField(default=5)
    balance_initialisation = models.IntegerField()
    objectif = models.PositiveSmallIntegerField(default=100)
    mois = ManyToManyField(
        'compte.Compte',
        through='ExerciceCompte',
        through_fields=('exercice', 'compte')
    )

    def __repr__(self):
        return f"{self.id}"


class ExerciceCompte(models.Model):
    exercice = models.ForeignKey('Exercice', on_delete=models.DO_NOTHING)
    compte = models.ForeignKey('compte.Compte', on_delete=models.DO_NOTHING)
