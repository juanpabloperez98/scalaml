from django.urls import path
from .views import *

app_name = 'expressions'

urlpatterns = [
    path('expresiones', expressions.as_view(), name = 'main'),
    path('expresiones/ejemplo1', ejemplo1.as_view(), name = 'ejemplo1'),
    path('expresiones/ejemplo2', ejemplo2.as_view(), name = 'ejemplo2'),
    path('expresiones/ejemplo3', ejemplo3.as_view(), name = 'ejemplo3'),
    path('expresiones/ejemplo4', ejemplo4.as_view(), name = 'ejemplo4'),
]