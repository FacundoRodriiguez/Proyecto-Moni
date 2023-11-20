from django.db import models

#formulario de datos de persona
class Persona(models.Model):
    dni = models.IntegerField()
    nombre_y_apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    monto_solicitado = models.IntegerField()
    def __str__(self):
        return self.nombre_y_apellido 
        
#formulario de datos de usuario    
class usuario(models.Model):
    nombre  = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
        

