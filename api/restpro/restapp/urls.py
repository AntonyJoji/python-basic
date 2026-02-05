
from django.urls import path

from restapp.views import userprofile

urlpatterns = [
    path('ser/', userprofile.as_view()),
]
