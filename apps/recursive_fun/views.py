from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class recursive_fun(TemplateView):
    template_name = "recursive_fun/index.html"