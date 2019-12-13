from django import forms
from django.forms import Select, NumberInput, DateInput, TimeInput

from compte.models import Compte
from operation.models import Operation


SEX_CHOICES = [
    ('depot', 'Masculin'),
    ('F',      'Féminin')
]

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = '__all__'

        widgets = {
            'compte': Select(
                attrs={
                    'class': 'form-control',
                },
                choices=Compte.objects.all()
            ),
            'type_operation': Select(
                attrs={
                    'class': 'form-control',
                },
            ),
            'montant': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ex: 200000",
                }
            ),
            'date': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
        }