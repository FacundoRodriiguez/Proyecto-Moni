from django.contrib import admin
from django.urls import path, include
# path: prestamo/urls.py
urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('web.urls')),
]
