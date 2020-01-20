from datetime import datetime, timedelta, date

from django import template

register = template.Library()


@register.filter
def somme(value):
    return sum(value)
