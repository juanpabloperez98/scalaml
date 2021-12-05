from django.urls import path
from .views import *

app_name = 'expresiones_regulares'

urlpatterns = [
    path('expresiones_regulares', Main.as_view(), name = 'main'),
]