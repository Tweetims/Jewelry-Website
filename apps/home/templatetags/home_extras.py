from django import template

register = template.Library()


@register.simple_tag
def multiply3(value, wax, metal):
    return f'{value * wax * metal:.2f}'

@register.simple_tag
def multiply2(value1, value2):
    return f'{value1 * value2:.2f}'
