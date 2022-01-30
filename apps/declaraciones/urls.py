from django.urls import path
from .views import *

app_name = 'declaraciones'

urlpatterns = [
    path('declaraciones', declaraciones.as_view(), name = 'main'),
    path('declaraciones/ejemplo1', declaraciones_ejemplo_1.as_view(), name = 'declaraciones_ejemplo1'),
    path('declaraciones/ejemplo2', declaraciones_ejemplo_2.as_view(), name = 'declaraciones_ejemplo2'),
]