from django import template

register = template.Library()

@register.filter(name='kut')
def kut(value, arg):
    """This cuts all the "arg" from given string "value" """
    return value.replace(arg,'')

# register.filter('kut',kaat)
