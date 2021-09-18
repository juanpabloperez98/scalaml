from django.urls import path
from .views import *

app_name = 'main_app'

urlpatterns = [
    path('', home.as_view(), name = 'main'),
]