from django.contrib import admin
from django.urls import path, re_path
from app.views import add_project

urlpatterns = [
path('add_project/', add_project),
]