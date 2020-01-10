from django import forms
from django.forms import Select, ModelForm, TextInput, EmailInput, FileInput, NumberInput

from investisseur.models import Investisseur


SEX_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin')
]

class InvestisseurForm(ModelForm):
    class Meta:
        model = Investisseur
        fields = ['first_name', 'last_name', 'email', 'telephone', 'sexe', 'parrain']

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
            'parrain': Select(
                attrs={
                    'class': "form-control",
                },
                choices=[]#Investisseur.objects.all(),
            ),
        }

class MDSelect(Select):
    pass