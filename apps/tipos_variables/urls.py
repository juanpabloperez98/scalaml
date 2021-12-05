from django.urls import path
from .views import *

app_name = 'tipos_variables'

urlpatterns = [
    path('tipos_variables', tipos_variables.as_view(), name = 'main'),
]