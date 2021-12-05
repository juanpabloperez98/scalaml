from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class tipos_variables(TemplateView):
    template_name = "tipos-variables/index.html"