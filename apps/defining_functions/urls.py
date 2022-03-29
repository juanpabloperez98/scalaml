from django.urls import path
from .views import *

app_name = 'defining_functions'

urlpatterns = [
    path('defining_functions', defining_functions.as_view(), name = 'main'),
]