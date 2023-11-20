from django.test import TestCase
import json
from .models import Prestamo
from decimal import Decimal

#creo la clase para el test y lo defino
class TestRegistrarPrestamo(TestCase):

    def test_prestamo(self):
        data = {
            'dni': '41888777',
            'nombre_apellido': 'luis',
            'genero': 'masculino',
            'email': 'luis@gmail.com',
            'monto_solicitado': '20000'
        }
        response = self.client.post("/api/prestamos/", data=json.dumps(data), content_type="application/json")
        prestamo = Prestamo.objects.all().first()
        
        self.assertEqual(response.status_code, 200)
        
        self.assertEqual(prestamo.dni, '41888777')
        self.assertEqual(prestamo.nombre_apellido, 'luis')
        self.assertEqual(prestamo.genero, 'masculino')
        self.assertEqual(prestamo.email, 'luis@gmail.com')
        self.assertEqual(prestamo.monto_solicitado, Decimal('20000.00'))

        self.assertIn(prestamo.aprobado, [False, True])

