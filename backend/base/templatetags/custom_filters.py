from django import template

register = template.Library()

@register.filter
def getattribute(obj, attr_name):
    return getattr(obj, attr_name, None)

@register.filter
def cycle_colors(index):
    colors = ["orange", "yellow", "red", "violet", "green", "tomato","pink"]
    return colors[index % len(colors)]