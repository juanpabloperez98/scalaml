from django.urls import path
from .views import *


app_name = 'tuples_lists'

urlpatterns = [
    path('tuples_lists', tuples_lists.as_view(), name = 'main'),
    path('tuples_lists/ejemplo1', ejemplo1.as_view(), name = 'ejemplo1'),
    path('tuples_lists/ejemplo2', ejemplo2.as_view(), name = 'ejemplo2'),
]