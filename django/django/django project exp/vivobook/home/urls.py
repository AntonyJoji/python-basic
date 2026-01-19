
from django.urls import include, path
from .views import *
urlpatterns = [
    path('homecall',homecall),
    path('',home),
    path('addval/',addval),
]