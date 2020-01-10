from django import forms
from django.forms import TextInput, Select, NumberInput, DateInput

from compte.models import Compte
from tradeur.models import Tradeur


class CompteForm(forms.ModelForm):
    class Meta:
        model = Compte
        fields = ['num_compte', 'broker', 'tradeur', 'montant_investi', 'date_creation']

        widgets = {
            'num_compte': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "XXXXX-XXXXX-XXXXX",
                },
            ),
            'tradeur': Select(
                attrs={
                    'class': 'form-control',
                    # 'required': False,
                },
                choices=[]#Tradeur.objects.all(),
            ),
            'broker': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
                choices=[]#Tradeur.objects.all()
            ),
            'montant_investi': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "200000",
                }
            ),
            'date_creation': DateInput(
                attrs={
                    'class': 'form-control',
                    'required': False,
                    'type': 'date',
                }
            ),
        }