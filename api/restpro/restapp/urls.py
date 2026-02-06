
from django.urls import path

from restapp.views import *

urlpatterns = [
    path('ser/', userprofile.as_view()),
    path('ser/<int:key>/', profile.as_view())
    
]
