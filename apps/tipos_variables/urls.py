from django.urls import path
from .views import *

app_name = 'tipos_variables'

urlpatterns = [
    path('tipos_variables', tipos_variables.as_view(), name = 'main'),
    path('tipos_variables/ejemplo1', tipo_variables_ejemplo1.as_view(), name = 'ejemplo1'),
    path('tipos_variables/ejemplo2', tipo_variables_ejemplo2.as_view(), name = 'ejemplo2'),
    path('tipos_variables/ejemplo3', tipo_variables_ejemplo3.as_view(), name = 'ejemplo3'),
    path('tipos_variables/ejercicios', ejercicios.as_view(), name = 'ejercicios'),
    
]