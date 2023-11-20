from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Prestamo
from .serializers import PrestamoSerializer
import requests
from rest_framework import status
from rest_framework.authtoken.models import Token
from .forms import CustomAuthenticationForm
from .models import CustomUsers
from .serializers import CustomUsersSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView

#creo la clase login para que me devuelva el token
class Login(APIView):
    def post(self, request, format=None):
        form = CustomAuthenticationForm(data=request.data)
        if form.is_valid():
            user = form.get_user()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            print(form.errors)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

#creo la clase logout para que me elimine el token
@api_view(['GET'])
@permission_classes([IsAdminUser])
def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    serializer = PrestamoSerializer(prestamos, many=True)
    return Response(serializer.data)

#creo get y post para que me devuelva los datos y me guarde los datos
@api_view(['GET','POST'])
def prestamo_api_view(request):
    if request.method == 'GET':
        prestamos = Prestamo.objects.all()
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data)
   
    elif request.method == 'POST':
        prestamo = PrestamoSerializer(data = request.data)
        if prestamo.is_valid():
            # Llamada a la API Moni para scoring
            moni_api_url = f'https://api.moni.com.ar/api/v4/scoring/pre-score/{prestamo.validated_data["dni"]}'
            headers = {'credential': 'ZGpzOTAzaWZuc2Zpb25kZnNubm5u'}
            moni_response = requests.get(moni_api_url, headers=headers)
            moni_data = moni_response.json()
            aprobado = moni_data.get('status', False) == 'approve'
            prestamo.validated_data["aprobado"] = aprobado
            prestamo.save()
            
            return Response(prestamo.data)
    return Response(prestamo.errors)

#creo get, delete y patch para que me devuelva los datos, me elimine los datos y me actualice los datos
@api_view(['DELETE','PATCH'])
def prestamo_delete(request,id):
    prestamo = Prestamo.objects.filter(id=id).first()
    if request.method == 'DELETE':
        prestamo.delete()
        return Response('Prestamo eliminado')
    elif request.method == 'PATCH':
        prestamo.dni = request.data.get('dni', prestamo.dni)
        prestamo.nombre_apellido = request.data.get('nombre_apellido', prestamo.nombre_apellido)
        prestamo.genero = request.data.get('genero', prestamo.genero)
        prestamo.email = request.data.get('email', prestamo.email)
        prestamo.monto_solicitado = request.data.get('monto_solicitado', prestamo.monto_solicitado)
        prestamo.save()
        return Response('Prestamo actualizado')
    return Response('Prestamo no encontrado')