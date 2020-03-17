from datetime import date

from django.db import models

from compte.models import Compte
from investissement.utils import incrementer_date
from investisseur.models import Investisseur

POURCENTAGE_BONUS = .05
POURCENTAGE_MENSUEL = .4
MONTH_LENGTH = 30
TYPE_CHOICES = [
    ('B', 'Bloqué'),
    ('M', 'Mensuel')
]


class Investissement(models.Model):
    investisseur = models.ForeignKey(Investisseur, related_name='investissements', on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_investissement = models.DateField(default=date.today)
    date_decompte = models.DateField(default=date.today)
    duree = models.PositiveSmallIntegerField(default=1)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)

    class Meta:
        ordering = ['date_decompte']

    def __str__(self):
        # self.refresh_status_payements()

        return f"investissement n° {self.id}"

    def supprimer_payements(self):
        from payement.models import Payement
        # self.refresh_status_payements()

        payements = Payement.objects.filter(investissement=self)
        for payement in payements:
            payement.delete()

    def generer_payements(self):
        from payement.models import Payement
#         # self.refresh_status_payements()

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
                montant=montant_payement
            )

            payement.investissement = self
            payement.save()

    def is_finish(self):
        # self.refresh_status_payements()

        today = date.today()
        invest_end = incrementer_date(self.date_decompte, 30 * self.duree)

        return today > invest_end

    def payement_courant(self):
        # self.refresh_status_payements()

        payement = self.payements.filter(status="NP").order_by('date').first()
        return payement

    def payements_termines(self):
        # self.refresh_status_payements()

        payements = self.payements.filter(status__in=("VR", "RE", "EC")).order_by('date')
        return payements

    def refresh_status_payements(self):
        payements = list(self.payements.filter(status="NP")) + list(self.payements.filter(status=None))

        for payement in payements:
            if payement.date < date.today():
                payement.status = "EC"
                payement.save()
            elif payement.debut_payement() < date.today():
                payement.status = "NP"
                payement.save()

    def bonus(self):
        return float(self.montant) * POURCENTAGE_BONUS

    def pourcentage_rsi(self):
        return self.retour_sur_investissement() * 100 / float(self.montant)

    def pourcentage(self):
        aujourdhui = date.today()

        if aujourdhui >= self.date_fin():
            return 100

        return int((aujourdhui - self.date_decompte).days * 100 / float(MONTH_LENGTH * self.duree))

    def retour_sur_investissement(self):
        return float(self.montant) * (1 + (POURCENTAGE_MENSUEL * self.duree))

    def date_fin(self):
        return incrementer_date(self.date_decompte, MONTH_LENGTH * self.duree)

    def rang(self):
        rank = 1
        investissements = self.__class__.objects.filter(investisseur=self.investisseur)

        for i in range(len(investissements)):
            if investissements[i].id == self.id:
                return i + 1
        return rank
