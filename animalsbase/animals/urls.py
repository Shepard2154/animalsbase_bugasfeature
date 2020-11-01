from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('<int:animal_id>/', get_animal),
]
