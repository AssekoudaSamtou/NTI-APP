from django.forms import Form, TextInput, Select, FileInput, NumberInput, EmailInput
from django import forms

from exercice.models import Exercice


DUREE_CHOICES = [
    ('5', '5 Mois'),
    ('4', '4 Mois'),
    ('3', '3 Mois'),
    ('2', '2 Mois'),
    ('1', '1 Mois'),
]

class ExerciceForm(forms.ModelForm):
    class Meta:
        model = Exercice
        fields = "__all__"

        widgets = {
            'nom': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "ex: xmed-furtif",
                },
            ),
            'date_debut': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date'
                },
            ),
            'duree': Select(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'disabled': 'disabled',
                },
                choices=DUREE_CHOICES
            ),
            'balance_initialisation': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "ex : 200000",
                }
            ),
            'objectif': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'disabled': 'disabled',
                }
            ),
        }
