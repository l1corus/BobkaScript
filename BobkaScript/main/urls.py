from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main_page'),
    path('docs', docs, name='docs'),
    path('about', about, name='about'),
]
