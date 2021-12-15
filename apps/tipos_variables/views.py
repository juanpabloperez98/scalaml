from django.shortcuts import render

# Create your views here.
from django.views.generic import(
    TemplateView
)


class tipos_variables(TemplateView):
    template_name = "tipos-variables/index.html"

class tipo_variables_ejemplo1(TemplateView):
    template_name = "tipos-variables/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['page'] = 2
        return context
    
