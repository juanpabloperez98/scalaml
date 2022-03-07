from django.shortcuts import render



from django.views.generic import(
    TemplateView
)

# Create your views here.

class type_consistency(TemplateView):
    template_name = "type_consistency/index.html"

class ejemplo1(TemplateView):
    template_name = "type_consistency/ejemplos/ejemplo1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 1
        context['page'] = 2
        return context

class ejemplo2(TemplateView):
    template_name = "type_consistency/ejemplos/ejemplo2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['example'] = True
        context['num_example'] = 2
        context['page'] = 2
        return context
