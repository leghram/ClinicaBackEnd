from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class ControlCreacionUsuarios(BaseUserManager):
    def create_user(self, nombre, apellido, correo, password):
        if not correo:
            raise ValueError('el usuario necesita un correo')
        correo = self.normalize_email(correo)
        nuevoUsuario = self.model(correo= correo, nombre = nombre, apellido = apellido)
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    def create_superuser(self,nombre, apellido, correo, password):
        nuevoUsuario = self.create_user(correo, nombre, apellido, password)
        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.is_active = True
        nuevoUsuario.save()





class Usuario(AbstractBaseUser):
    id= models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=70)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField(unique=True)
    password = models.TextField(db_column='contrasena', max_length=50)

    is_staff = models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)

    objects = ControlCreacionUsuarios()

    USERNAME_FIELD = 'correo'


    REQUIRED_FIELDS= ['nombre','apellido']

    class Meta:
        db_table = 'usuarios'
