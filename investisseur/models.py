from django.contrib.auth.models import User
from django.db import models

PAYEMENT_CHOICES = [
	('flooz', 'Flooz'),
	('tmoney', 'T-Money'),
	('banque', 'Compte Bancaire'),
]

class Investisseur(User):
	telephone = models.CharField(max_length=20, unique=True)
	sexe = models.CharField(max_length=1)
	parrain = models.ForeignKey('Investisseur', related_name='fieuls', on_delete=models.CASCADE, null=True, blank=True)
	init_password = models.CharField(max_length=50)
	mode_payement = models.CharField(max_length=7, choices=PAYEMENT_CHOICES, null=True)
	# avatar = models.ImageField(upload_to="photos/", null=True, blank=True)

	def __repr__(self):
		return f"{self.first_name} {self.last_name}"

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

	def has_changed_init_pwd(self):
		return self.check_password(self.init_password) == False
