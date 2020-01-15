from django import template

register = template.Library()

@register.filter
def somme(value):
	return sum(value)
