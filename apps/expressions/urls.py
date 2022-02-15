from django.urls import path
from .views import *

app_name = 'expressions'

urlpatterns = [
    path('expresiones', expressions.as_view(), name = 'main'),
]