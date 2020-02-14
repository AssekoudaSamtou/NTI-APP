from django.forms import ModelForm, TextInput, EmailInput, NumberInput, PasswordInput

from investisseur.models import Investisseur


class UpdateInfosPersoForm(ModelForm):
    class Meta:
        model = Investisseur
        fields = ['first_name', 'last_name', 'username']

        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control names',
                    'required': True
                },
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control names',
                    'required': True
                },
            ),
            'username': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                },
            )
        }

class UpdateContactForm(ModelForm):
    class Meta:
        model = Investisseur
        fields = ['email', 'telephone']

        widgets = {
            'email': EmailInput(
                attrs={
                    'class': "form-control",
                    'required': True
                }
            ),
            'telephone': NumberInput(
                attrs={
                    'class': "form-control",
                    'required': True
                }
            ),
        }

class UpdatePasswordForm(ModelForm):
    class Meta:
        model = Investisseur
        fields = ['email', 'telephone']

        widgets = {
            'email': PasswordInput(
                attrs={
                    'class': "form-control",
                    'required': True,
                }
            ),
        }
