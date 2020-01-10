from django.contrib import admin

from compte.models import Mois
from exercice.models import Exercice, ExerciceCompte

admin.site.register(Exercice)
admin.site.register(ExerciceCompte)
admin.site.register(Mois)
