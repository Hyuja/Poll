from django import template

register = template.Library()

@register.simple_tag(name="DoubleIndex")
def DoubleIndex(parental_forloop, allvotes, vote):
    return round(vote/(allvotes[parental_forloop])*100, 2)