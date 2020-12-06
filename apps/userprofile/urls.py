from django.urls import path, include

from .views import dashboard

urlpattern = [
    path('', dashboard, name='dashboard'),
]