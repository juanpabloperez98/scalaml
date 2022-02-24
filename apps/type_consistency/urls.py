from django.urls import path
from .views import *


app_name = 'type_consistency'

urlpatterns = [
    path('type_consistency', type_consistency.as_view(), name = 'main')
]