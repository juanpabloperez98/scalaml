from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView


class tuples_lists(TemplateView):
    template_name = "tuples_lists/index.html"


class ejemplo1(TemplateView):
    template_name = "tuples_lists/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 1
        context['page'] = 3
        return context

class ejemplo2(TemplateView):
    template_name = "tuples_lists/ejemplos/ejemplo2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 2
        context['page'] = 3
        return context