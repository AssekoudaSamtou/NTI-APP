from django.forms import Form, TextInput, Select, FileInput, NumberInput, EmailInput, ModelForm
from django import forms

from tradeur.models import Tradeur

SEX_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin')
]


class Personne(Form):
    pass


class TradeurForm(ModelForm):
    class Meta:
        model = Tradeur
        fields = '__all__'

        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "John",
                },
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "Doe",
                },
            ),
            'email': EmailInput(
                attrs={
                    'class': "form-control",
                    'required': True,
                    'placeholder': "tradeur@exemple.com",
                }
            ),
            'telephone': NumberInput(
                attrs={
                    'class': "form-control",
                    'required': True,
                    'placeholder': "tradeur@exemple.com",
                }
            ),
            'sexe': Select(
                attrs={
                    'class': "form-control",
                    'required': True,
                },
                choices=SEX_CHOICES
            ),
            'avatar': FileInput(
                attrs={
                    'class': "form-control",
                }
            )
        }
