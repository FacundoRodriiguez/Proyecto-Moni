from django.urls import path
from .views import  prestamo_api_view
from .views import Login
from .views import prestamo_delete
#creo las urls para que me devuelva los datos, me elimine los datos y me guarde los datos
urlpatterns = [
    path('prestamos/', prestamo_api_view, name='prestamo_api_view'),
    path('',Login.as_view(), name = 'login'),
    path('prestamos/<int:id>/', prestamo_delete, name='prestamo_delete'),

]


