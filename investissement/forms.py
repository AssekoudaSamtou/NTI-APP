from django.forms import ModelForm, Select, NumberInput, DateInput, TextInput

from investisseur.models import Investisseur
from .models import Investissement

DUREE_CHOICES = [
    ('1', '1 Mois'),
    ('2', '2 Mois'),
    ('3', '3 Mois'),
    ('4', '4 Mois'),
    ('5', '5 Mois')
]

class InvestissementForm(ModelForm):
    class Meta:
        model = Investissement
        # fields = '__all__'
        exclude = ['duree', 'taux']

        widgets = {
            'date_decompte': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date'
                },
            ),
            'date_investissement': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date',
                },
            ),
            'montant': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
            ),
            'investisseur': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
            ),
            'pack': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
            ),
        }

    def clean(self):
        cleaned_data = super().clean()


class InvestissementForm2(ModelForm):
    class Meta:
        model = Investissement
        exclude = ['duree', 'taux']

        widgets = {
            'date_decompte': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date'
                },
            ),
            'date_investissement': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'type': 'date',
                },
            ),
            'montant': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'disabled': False,
                },
            ),
            'investisseur': Select(
                attrs={
                    'class': 'form-control disabled',
                    'required': True,
                    # 'disabled': True,
                },
                choices=[]
            ),
            'pack': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
            ),
        }
