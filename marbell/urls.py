from django.urls import path
from .views import *

urlpatterns = [
    path('main/', simple_index, name='main_page')
]