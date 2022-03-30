from django.urls import path
from .views import *

app_name = 'defining_functions'

urlpatterns = [
    path('defining_functions', defining_functions.as_view(), name = 'main'),
    path('defining_functions/ejemplo1', ejemplo1.as_view(), name = 'ejemplo1'),
    path('defining_functions/ejemplo2', ejemplo2.as_view(), name = 'ejemplo2'),
]