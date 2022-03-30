from django.conf import settings
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView


class defining_functions(TemplateView):
    template_name = "defining_functions/index.html"

class ejemplo1(TemplateView):
    template_name = "defining_functions/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 1
        context['page'] = 4
        return context

class ejemplo2(TemplateView):
    template_name = "defining_functions/ejemplos/ejemplo2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 2
        context['page'] = 4
        return context