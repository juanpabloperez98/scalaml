from django.conf import settings
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView


class defining_functions(TemplateView):
    template_name = "defining_functions/index.html"