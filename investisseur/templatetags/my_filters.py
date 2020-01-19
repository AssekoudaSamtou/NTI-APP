from datetime import datetime, timedelta, date

from django import template

register = template.Library()


@register.filter
def somme(value):
    return sum(value)


@register.filter
def payement_date(investissement):
    payement = investissement.payements.filter(status=None).order_by('date').first()
    return payement.date


@register.filter
def payement_number(investissement):
    numero = 1
    payements = investissement.payements.all()
    for i in range(len(payements)):
        if payements[i].status not in ('VR', 'RE'):
            return i + 1
    return numero


@register.filter
def percentage(investissement):
    payement = investissement.payements.filter(status=None).order_by('date').first()
    print(payement.date)
    print(date.today())
    temps_ecoule = timedelta(days=30) - (payement.date - date.today())
    poucentage = temps_ecoule.days * 100 / 30
    return poucentage


@register.filter
def global_percentage(investissement):
    pass


@register.filter
def debut_payement(investissement):
    return payement_date(investissement) - timedelta(days=30)
