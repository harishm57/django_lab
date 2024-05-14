from django.urls import path
from . import views
urlpatterns = [
     path('current-datetime/', views.current_datetime,name='current-datetime'),
]