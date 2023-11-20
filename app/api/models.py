from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group, Permission

# creo mi modelo de datos para la tabla prestamo con sus campos
class Prestamo(models.Model):
    dni = models.CharField(max_length=10)
    nombre_apellido = models.CharField(max_length=255)
    genero = models.CharField(max_length=10)
    email = models.EmailField()
    monto_solicitado = models.DecimalField(max_digits=10, decimal_places=2)
    aprobado = models.BooleanField(default=False)

# creo mi modelo de datos para la tabla usuario con sus campos
class CustomUsers(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=True)
    REQUIRED_FIELDS = ['email', 'password']
    USERNAME_FIELD = 'usuario'
    EMAIL_FIELD = 'email'

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customusers",
        related_query_name="user",
    )

# creo mi modelo de datos para la tabla permiso con sus campos
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customusers",
        related_query_name="user",
    )

