from django.contrib import admin
from django.urls import path
from simplemooc.courses.views import index, details

app_name='courses'

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>/', details, name='details'),
]
