from django.forms import ModelForm, Select, NumberInput, DateInput

from payement.models import Payement


class PayementForm(ModelForm):
    class Meta:
        model = Payement
        fields = '__all__'

        widgets = {
            'investissement': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
            ),
            'date': DateInput(
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
                    'placeholder': "Ex: 300000",
                    'disabled': False,
                },
            ),
            'status': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
            )
        }

    def clean(self):
        cleaned_data = super().clean()

