from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class recursive_fun(TemplateView):
    template_name = "recursive_fun/index.html"


class ejemplo1(TemplateView):
    template_name = "recursive_fun/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 1
        context['page'] = 5
        return context

class ejemplo2(TemplateView):
    template_name = "recursive_fun/ejemplos/ejemplo2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 2
        context['page'] = 5
        return context

class ejemplo3(TemplateView):
    template_name = "recursive_fun/ejemplos/ejemplo3.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 3
        context['page'] = 5
        return context

