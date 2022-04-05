from django.urls import path
from .views import *


app_name = 'recursive_fun'

urlpatterns = [
    path('recursive_fun', recursive_fun.as_view(), name = 'main'),
]