from django import template

register = template.Library()


@register.filter(name='Censor')
def Censor(value, arg):
    return value.replace(arg, '*' * len(arg))

# @register.filter(name='Censor')
# def Censor(value):
#     censor_list = ['art', 'some', 'new', 'text']
#     for arg in censor_list:
#         value = value.replace(arg, '*' * len(arg))
#     return value
