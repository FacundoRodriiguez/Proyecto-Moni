from rest_framework import serializers
from .models import Prestamo, CustomUsers

#creo la clase PrestamoSerializer para que me devuelva los datos
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ['id','dni', 'nombre_apellido', 'genero', 'email', 'monto_solicitado', 'aprobado']

#creo la clase CustomUsersSerializer para que me devuelva los datos
class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsers
        fields = [ 'email', 'password', 'is_admin']