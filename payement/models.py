from datetime import date, timedelta

from django.db import models

from investissement.models import Investissement

STATUS_CHOICES = [
    ('NP', 'Non Payé'),
    ('EC', 'En Cours'),
    ('VR', 'Virement Effectué'),
    ('RE', 'Reçu'),
]


class Payement(models.Model):

    investissement = models.ForeignKey(Investissement, related_name='payements', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    montant = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=True)

    class Meta:
        ordering = ['date']

    def __repr__(self):
        return f"Payement n° {self.id}"

    def debut_payement(self):
        return self.date - timedelta(days=30)

    def pourcentage(self):
        if date.today() >= self.date:
            return 100
        if date.today() <= self.debut_payement():
            return 0
        temps_ecoule = timedelta(days=30) - (self.date - date.today())
        pourcentage = temps_ecoule.days * 100 / 30
        return int(pourcentage)

    def rang(self):
        rank = 1
        payements = self.__class__.objects.filter(investissement=self.investissement)
        print(payements)
        for i in range(len(payements)):
            if payements[i].id == self.id:
                return i + 1
        return rank

    def formed_img_name(self):
        return f'img/icons8_calendar_{self.rang()}_48px.png'
