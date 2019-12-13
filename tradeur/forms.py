from django.forms import Form, TextInput, Select, FileInput, NumberInput, EmailInput
from django import forms


SEX_CHOICES = [
    ('M', 'Masculin'),
    ('F', 'Féminin')
]

class Personne(Form):
    nom = forms.CharField(
        max_length=50,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': "John",
            },
        ),
    )
    prenom = forms.CharField(
        max_length=50,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': "Doe",
            },
        ),
    )
    email = forms.EmailField(
        max_length=225,
        widget=EmailInput(
            attrs={
                'class': "form-control",
                'required': True,
                'placeholder': "tradeur@exemple.com",
            }
        )
    )
    telephone = forms.IntegerField(
        widget=NumberInput(
            attrs={
                'class': "form-control",
                'required': True,
                'placeholder': "0022893870335",
            }
        ),
    )
    sexe = forms.CharField(
        max_length=1,
        widget=Select(
            attrs={
                'class': "form-control",
                'required': True,
                'placeholder': "tradeur@exemple.com",
            },
            choices=SEX_CHOICES
        ),
    )
    def clean(self):
        cleaned_data = super().clean()
    # self.add_error("username", "error")
    # raise forms.ValidationError(
    # 			"Did not send for 'help' in the subject despite "
    # 			"CC'ing yourself."
    #		)



class TradeurForm(Personne):

    avatar = forms.ImageField(
        widget=FileInput(
            attrs={
                'class': "form-control",
                'required': False,
            }
        ),
    )


