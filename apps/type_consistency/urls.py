from django.urls import path
from .views import *


app_name = 'type_consistency'

urlpatterns = [
    path('type_consistency', type_consistency.as_view(), name = 'main'),
    path('type_consistency/ejemplo1', ejemplo1.as_view(), name = 'ejemplo1'),
    path('type_consistency/ejemplo2', ejemplo2.as_view(), name = 'ejemplo2'),
    path('type_consistency/ejercicios', ejercicios.as_view(), name = 'ejercicios')
]