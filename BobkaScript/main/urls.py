from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', main_page, name='main_page'),
    path('docs', docs, name='docs'),
    path('about', about, name='about'),
]

urlpatterns += staticfiles_urlpatterns()
