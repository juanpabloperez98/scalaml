from django.shortcuts import render



from django.views.generic import(
    TemplateView
)

# Create your views here.

class type_consistency(TemplateView):
    template_name = "type_consistency/index.html"
