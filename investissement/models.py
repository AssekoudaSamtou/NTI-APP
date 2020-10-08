from datetime import date, datetime

from django.contrib.auth.models import User
from django.db import models, transaction

from compte.models import Compte
from investissement.utils import incrementer_date
from investisseur.models import Investisseur

POURCENTAGE_BONUS = .05
POURCENTAGE_MENSUEL = .3
MONTH_LENGTH = 30
PACK_CHOICES = [
    ('1', 'Profit Mensuel'),
    ('2', 'Bloqué')
]

class Pack(models.Model):
    libelle = models.CharField(max_length=14)
    duree = models.PositiveSmallIntegerField()
    taux = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return f"Pack 0{self.id} ({self.libelle})"

class Investissement(models.Model):
    investisseur = models.ForeignKey(Investisseur, related_name='investissements', on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_investissement = models.DateField(default=date.today)
    date_decompte = models.DateField(default=date.today)
    pack = models.ForeignKey(Pack, related_name='investissements', on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date_decompte']

    def __str__(self):
        return f"investissement n° {self.id}"

    def supprimer_payements(self):
        from payement.models import Payement

        payements = Payement.objects.filter(investissement=self)
        for payement in payements:
            payement.delete()

    def generer_payements(self):
        from payement.models import Payement

        with transaction.atomic():
            base_date = self.date_decompte
            for i in range(self.pack.duree):

                if i + 1 == self.pack.duree:
                    montant_payement = float(self.montant) * 1.4
                else:
                    montant_payement = float(self.montant) * 0.4

                base_date = incrementer_date(base_date, 30)
                payement = Payement(
                    investissement=self,
                    date=base_date,
                    montant=montant_payement
                )

                payement.investissement = self
                payement.save()

    def is_finish(self):
        today = date.today()
        invest_end = incrementer_date(self.date_decompte, 30 * self.pack.duree)

        return today > invest_end

    def payement_courant(self):
        payement = self.payements.filter(status="NP").order_by('date').first()
        return payement

    def payements_termines(self):
        payements = self.payements.filter(status__in=("VR", "RE", "EC")).order_by('date')
        return payements

    def bonus(self):
        return float(self.montant) * POURCENTAGE_BONUS

    def pourcentage_rsi(self):
        return self.retour_sur_investissement() * 100 / float(self.montant)

    def pourcentage(self):
        aujourdhui = date.today()

        if aujourdhui >= self.date_fin():
            return 100

        return int((aujourdhui - self.date_decompte).days * 100 / float(MONTH_LENGTH * self.pack.duree))

    def retour_sur_investissement(self):
        return float(self.montant) * (1 + (POURCENTAGE_MENSUEL * self.pack.duree))

    def date_fin(self):
        return incrementer_date(self.date_decompte, MONTH_LENGTH * self.pack.duree)

    def rang(self):
        rank = 1
        investissements = self.__class__.objects.filter(investisseur=self.investisseur)

        for i in range(len(investissements)):
            if investissements[i].id == self.id:
                return i + 1
        return rank
