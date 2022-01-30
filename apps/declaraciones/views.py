from django.shortcuts import render
from django.views.generic import(
    TemplateView
)
# Create your views here.

class declaraciones(TemplateView):
    template_name = "declaraciones/index.html"

class declaraciones_ejemplo_1(TemplateView):
    template_name = "declaraciones/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 1
        context['page'] = 3
        return context

class declaraciones_ejemplo_2(TemplateView):
    template_name = "declaraciones/ejemplos/ejemplo2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 2
        context['page'] = 3
        return context
