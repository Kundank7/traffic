# traffic/urls.py

from django.urls import path
from .views import generate_traffic

urlpatterns = [
    path('', generate_traffic, name='generate_traffic'),
]
