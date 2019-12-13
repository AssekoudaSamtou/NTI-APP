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
                    'placeholder': "300000",
                    'disabled': True,
                },
            ),
            'duree': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "01 mois",
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

class M_InvestissementForm(ModelForm):

    class Meta:
        model = Investissement
        fields = '__all__'

        widgets = {
            'date_decompte': DateInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Maintenant",
                    'type': 'date',
                    'disabled': True,
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
                    'placeholder': "300000",
                    'disabled': True,
                },
            ),
            'duree': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "01 mois",
                },
            ),
            'investisseur': Select(
                attrs={
                    'class': 'form-control',
                    'disabled': True,
                },
                choices= Investisseur.objects.all()
            ),
            # 'investisseur': TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'disabled': True,
            #         'value': f"amza"
            #     }
            # ),
        }

    def clean(self):
        cleaned_data = super().clean()
