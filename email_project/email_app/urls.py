# email_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email, name='send_email'),
]
