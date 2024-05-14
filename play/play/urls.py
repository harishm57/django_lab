
from django.contrib import admin
from django.urls import path 
from django.urls import path,include
from ground.views import current_datetime
urlpatterns=[
    path('',current_datetime,name='home'),
    path('ground/',include('ground.urls')),
    path('admin/',admin.site.urls),
    path('',include('ground.urls')),
]