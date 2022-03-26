from django.urls import path
from .views import *


app_name = 'tuples_lists'

urlpatterns = [
    path('tuples_lists', tuples_lists.as_view(), name = 'main'),
    path('tuples_lists/ejemplo1', ejemplo1.as_view(), name = 'ejemplo1'),
    path('tuples_lists/ejemplo2', ejemplo2.as_view(), name = 'ejemplo2'),
    path('tuples_lists/ejemplo3', ejemplo3.as_view(), name = 'ejemplo3'),
    path('tuples_lists/ejemplo4', ejemplo4.as_view(), name = 'ejemplo4'),
    path('tuples_lists/ejemplo5', ejemplo5.as_view(), name = 'ejemplo5'),
    path('tuples_lists/ejercicios', ejercicios.as_view(), name = 'ejercicios')
]