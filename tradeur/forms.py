from django.forms import Form, TextInput, Select, FileInput, NumberInput, EmailInput, ModelForm

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
        fields = ['first_name', 'last_name', 'email', 'telephone', 'sexe', 'avatar', 'username']

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
                    'placeholder': "0022893780353",
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
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "ex : DoeJhon",
                    # 'disabled': 'disabled'
                },
            ),
        }
