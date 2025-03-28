from django.urls import path
from .views import *

urlpatterns = [
    path('main/', simple_index, name='main_page'),
    path('main/es/', simple_index_spain, name='main_page_es')
]