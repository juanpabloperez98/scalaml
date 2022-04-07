from django.urls import path
from .views import *


app_name = 'recursive_fun'

urlpatterns = [
    path('recursive_fun', recursive_fun.as_view(), name = 'main'),
    path('recursive_fun/ejemplo1', ejemplo1.as_view(), name = 'ejemplo1'),
]