from django.urls import path
from .views import *


app_name = 'tuples_lists'

urlpatterns = [
    path('tuples_lists', tuples_lists.as_view(), name = 'main'),
]