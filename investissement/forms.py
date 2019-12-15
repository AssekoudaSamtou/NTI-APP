from django.forms import ModelForm, Select, NumberInput, DateInput, TextInput

from investisseur.models import Investisseur
from .models import Investissement


class InvestissementForm(ModelForm):
    class Meta:
        model = Investissement
        fields = '__all__'

        widgets = {
            'date_decompte': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "Maintenant",
                    'type': 'date'
                },
            ),
            'date_investissement': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "Maintenant",
                    'type' : 'date',
                },
            ),
            'montant': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "Ex: 300000",
                    'disabled': False,
                },
            ),
            'duree': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'min': 1,
                    'max': 5
                },
            ),
            'investisseur': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
                choices=Investisseur.objects.all()
            ),
        }

    def clean(self):
        cleaned_data = super().clean()

