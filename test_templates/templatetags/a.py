from django import template


register = template.Library()

from .b import *


@register.simple_tag
def say_a():
    return 'a'