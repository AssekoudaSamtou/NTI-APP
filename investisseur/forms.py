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
        fields = ['first_name', 'last_name', 'email', 'telephone', 'sexe', 'parrain', 'username']

        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control names',
                    'required': True,
                    'placeholder': "John",
                },
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control names',
                    'required': True,
                    'placeholder': "Doe",
                },
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "ex : DoeJhon",
                    # 'disabled': 'disabled'
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
            ),
        }

class InvestisseurFormDisabled(ModelForm):
    class Meta:
        model = Investisseur
        fields = ['first_name', 'last_name', 'email', 'telephone', 'sexe', 'parrain', 'username']

        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control names',
                    'required': True,
                    'placeholder': "John",
                    'disabled': 'disabled'
                },
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control names',
                    'required': True,
                    'placeholder': "Doe",
                    'disabled': 'disabled'
                },
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "ex : DoeJhon",
                    'disabled': 'disabled'
                },
            ),
            'email': EmailInput(
                attrs={
                    'class': "form-control",
                    'required': True,
                    'placeholder': "client@exemple.com",
                    'disabled': 'disabled'
                }
            ),
            'telephone': NumberInput(
                attrs={
                    'class': "form-control",
                    'required': True,
                    'placeholder': "client@exemple.com",
                    'disabled': 'disabled'
                }
            ),
            'sexe': Select(
                attrs={
                    'class': "form-control",
                    'required': True,
                    'disabled': 'disabled'
                },
                choices=SEX_CHOICES
            ),
            'parrain': Select(
                attrs={
                    'class': "form-control",
                    'disabled': 'disabled'
                },
            ),
        }

class MDSelect(Select):
    pass
