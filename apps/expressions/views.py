from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)

class expressions(TemplateView):
    template_name = "expressions/index.html"