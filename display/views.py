from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('users_display.html')
    return HttpResponse(template.render())
# Create your views here.
