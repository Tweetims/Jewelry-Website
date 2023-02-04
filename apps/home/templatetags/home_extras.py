from django import template

register = template.Library()


@register.simple_tag
def multiply(value, wax, metal):
    return f'{value * wax * metal:.2f}'
