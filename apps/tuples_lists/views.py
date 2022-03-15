from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class tuples_lists(TemplateView):
    template_name = "tuples_lists/index.html"