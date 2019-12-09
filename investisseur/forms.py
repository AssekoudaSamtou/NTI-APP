from django.forms import ModelForm, TextInput, Select, NumberInput

from .models import Investisseur

SEX_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin')
]


class InvestisseurForm(ModelForm):
    class Meta:
        model = Investisseur
        fields = ['email', 'nom', 'prenom', 'sexe', 'telephone']

        widgets = {
            'nom': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "John",
                },
            ),
            'prenom': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "Doe",
                },
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "user@example.com",
                },
            ),
            'telephone': NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': "0022898565751",
                },
            ),
            'sexe': Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                },
                choices=SEX_CHOICES
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
    # self.add_error("username", "error")
    # raise forms.ValidationError(
    # 			"Did not send for 'help' in the subject despite "
    # 			"CC'ing yourself."
    #		)
