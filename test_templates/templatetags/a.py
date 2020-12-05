from django import template

import b  # for PyCharm introspection: in a template doing '{% load a %}' to make {% say_b %} available

register = template.Library()


@register.simple_tag
def say_b(*args, **kwargs):
    return b.say_b(*args, **kwargs)


@register.simple_tag
def say_a():
    return 'a'
