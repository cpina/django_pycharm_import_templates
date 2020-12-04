from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    context = {}
    template = loader.get_template('test_templates/index.html')
    return HttpResponse(template.render(context, request))