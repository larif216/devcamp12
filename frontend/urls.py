from django.contrib import admin
from django.urls import path
from .views import main

app_name = 'frontend'
urlpatterns = [
    path('', main, name="main"),
]