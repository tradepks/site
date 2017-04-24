from django.template import Library


register = Library()

@register.filter
def getValue(dict, key):    
    try:
        return dict[key]
    except KeyError:
        return ''