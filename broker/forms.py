from django import forms
from django.forms import TextInput


class BrokerForm(forms.Form):
    libelle = forms.CharField(
        max_length=50,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': "ex: XM",
            },
        ),
    )
    site_web = forms.CharField(
        max_length=50,
        widget=TextInput(
            attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': "www.xm.com",
            },
        ),
    )
