from django.db import models
from django.db.models import ManyToManyField


class Exercice(models.Model):
    nom = models.CharField(max_length=225)
    date_debut = models.DateField()
    duree = models.PositiveSmallIntegerField(default=5)
    balance_initialisation = models.IntegerField()
    objectif = models.PositiveSmallIntegerField(default=500)
    comptes = ManyToManyField(
        'compte.Compte',
        through='ExerciceCompte',
        through_fields=('exercice', 'compte'),
        null=True
    )

    def __repr__(self):
        return f"{self.id}"


class ExerciceCompte(models.Model):
    exercice = models.ForeignKey('Exercice', on_delete=models.DO_NOTHING)
    compte = models.ForeignKey('compte.Compte', on_delete=models.DO_NOTHING)
