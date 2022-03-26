from django.conf import settings
from django.shortcuts import render
# Create your views here.
from django.views.generic import TemplateView


class expressions(TemplateView):
    template_name = "expressions/index.html"

class ejemplo1(TemplateView):
    template_name = "expressions/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 1
        context['page'] = 1
        return context

class ejemplo2(TemplateView):
    template_name = "expressions/ejemplos/ejemplo2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 2
        context['page'] = 1
        return context


class ejemplo3(TemplateView):
    template_name = "expressions/ejemplos/ejemplo3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 3
        context['page'] = 1
        return context

class ejemplo4(TemplateView):
    template_name = "expressions/ejemplos/ejemplo4.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 4
        context['page'] = 1
        return context

class ejercicios(TemplateView):
    template_name = "expressions/practica/practica.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['page'] = 1
        context['redirect_url'] = settings.URL_REDIRECT + "expressions"
        return context
    