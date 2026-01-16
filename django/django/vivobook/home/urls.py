
from django.urls import path
from .views import *
urlpatterns = [
    path('homecall', homecall),
    path('home/', home),
    path('addval/', addval),

]
