from django.urls import path
from .views import *

urlpatterns = [
    path('', simple_index, name='main_page'),
    path('es/', simple_index_spain, name='main_page_es')
]