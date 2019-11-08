from django.contrib import admin
from django.urls import path
from simplemooc.core.views import contact, home

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contact, name='contact'),
]
